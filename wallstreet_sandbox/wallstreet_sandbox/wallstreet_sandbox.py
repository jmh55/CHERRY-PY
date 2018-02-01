from wallstreet import Stock, Call, Put

s = Call('INTC', d=2, m=2, y=2018, strike=50, source='yahoo')

#for a, b in enumerate(s.strikes):
#    s.set_strike(b)
#    print(f'for option: {s.ticker} strike: {s.strike} bid: {s.bid} ask: {s.ask}')

print(s.underlying.ticker)
print(s.underlying.price)
print(s.strike)
print(f'price for {s.expiration}')
print(s.ask)
print(s.bid)

