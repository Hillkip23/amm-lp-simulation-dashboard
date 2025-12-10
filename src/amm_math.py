import numpy as np




def constant_product_price(x_reserve: float, y_reserve: float) -> float:
    """Return the AMM price y/x."""
    if x_reserve <= 0:
        raise ValueError("x_reserve must be positive")
    return y_reserve / x_reserve


def pool_reserves_from_price(k: float, price: float):
    """Given invariant k = x*y and target price p = y/x, solve for (x, y)."""
    if price <= 0:
        raise ValueError("price must be positive")
    x = np.sqrt(k / price)
    y = np.sqrt(k * price)
    return x, y




def impermanent_loss(price_rel):
    """Impermanent loss (no fees) as a function of relative price change R = P_t / P_0.

    Works with scalars, numpy arrays, and pandas Series/DataFrames.
    Formula: IL = 2*sqrt(R)/(1+R) - 1
    """
    return 2 * np.sqrt(price_rel) / (1 + price_rel) - 1


def lp_value_relative(price_rel: float) -> float:
    """LP position value relative to HODL, assuming no fees."""
    return 1.0 + impermanent_loss(price_rel)


def uniswap_v3_position_value(price: float, p_lower: float, p_upper: float, L: float = 1.0) -> float:
    """
    Value of a Uniswap v3 position (in token1 units) for a given price and range [p_lower, p_upper].

    We assume price is token1 per token0, and use the standard Uniswap v3 formulas.
    L is the liquidity parameter; since we only care about *relative* value, we can set L = 1.
    """
    if p_lower <= 0 or p_upper <= 0:
        raise ValueError("Price bounds must be positive")
    if p_lower >= p_upper:
        raise ValueError("p_lower must be < p_upper")

    sqrtP = np.sqrt(price)
    sqrtPa = np.sqrt(p_lower)
    sqrtPb = np.sqrt(p_upper)

    if price <= p_lower:
        # Entirely in token0
        amount0 = L * (sqrtPb - sqrtPa) / (sqrtPa * sqrtPb)
        amount1 = 0.0
    elif price >= p_upper:
        # Entirely in token1
        amount0 = 0.0
        amount1 = L * (sqrtPb - sqrtPa)
    else:
        # In-range mix
        amount0 = L * (sqrtPb - sqrtP) / (sqrtP * sqrtPb)
        amount1 = L * (sqrtP - sqrtPa)

    return amount0 * price + amount1


def lp_over_hodl_univ3(price_T: float, p_lower: float, p_upper: float, p0: float = 1.0) -> float:
    """
    Uniswap v3 LP performance vs 50/50 HODL at terminal price price_T.

    - Start with 50/50 HODL at price p0 (here p0 ~ 1).
    - LP provides concentrated liquidity in [p_lower, p_upper].
    - Returns LP_value_T / HODL_value_T.
    """
    # LP relative value (v3 position)
    v0 = uniswap_v3_position_value(p0, p_lower, p_upper, L=1.0)
    vT = uniswap_v3_position_value(price_T, p_lower, p_upper, L=1.0)
    lp_rel = vT / v0  # LP_T / LP_0

    # HODL relative value, starting 50/50 at p0
    R = price_T / p0
    hodl_rel = 0.5 * (1.0 + R)  # HODL_T / HODL_0 (HODL_0 = 1)

    return lp_rel / hodl_rel
