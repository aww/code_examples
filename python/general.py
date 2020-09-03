#
# Tools for manipulating IP addresses
#

# Source: https://en.wikipedia.org/wiki/Hilbert_curve
def rot(n, x, y, rx, ry):
    """Rotate/flip a quadraant appropriately"""
    if ry == 0:
        if rx == 1:
            x = n-1 - x
            y = n-1 - y
        #Swap x and y
        t = x
        x = y
        y = t
    return x, y

def ip_to_hilbert(ip):
    """Return x,y coordinates for mapping an ip address represented as a
       natural number<2**32 to a 2**16 x 2**16 square region using a Hilbert curve.
       This mapping is bijective as well as doing a good job of preserving locality."""
    n = 2**16
    d = ip
    t = d
    x, y = 0, 0
    s = 1
    while s < n:
        rx = 1 & (t//2);
        ry = 1 & (t ^ rx);
        x, y = rot(s, x, y, rx, ry);
        x += s * rx
        y += s * ry
        t //= 4
        s*=2
    return x, y

def ipstr(x):
    """Return a string representing an natural number < 2**32 the way IP addresses typically are,
       using decimal 8-bit components between dots."""
    return f'{x>>24}.{(x>>16)&255}.{(x>>8)&255}.{x&255}'

assert ipstr(3485268559) == '207.188.250.79'
assert ip_to_hilbert(3485268559) == (49604, 30479)
