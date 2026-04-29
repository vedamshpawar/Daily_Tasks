def current_holdings(transactions):
    AAPL = []
    GOOGL = []
    MSFT = []
    TSLA = []
    for tup in transactions:
        if tup[0] == 'AAPL':
            AAPL.append(tup)
        if tup[0] == 'GOOGL':
            GOOGL.append(tup)
        if tup[0] == 'MSFT':
            MSFT.append(tup)
        if tup[0] == 'TSLA':
            TSLA.append(tup)
    
    total_buy_AAPL = 0
    total_sell_AAPL = 0
    total_buy_GOOGL = 0
    total_sell_GOOGL = 0
    total_buy_MSFT = 0
    total_sell_MSFT = 0
    total_buy_TSLA = 0
    total_sell_TSLA = 0


    curr_hold_aapl = 0
    curr_hold_googl = 0
    curr_hold_msft = 0
    curr_hold_tsla = 0

    for tup in transactions:
        if tup[0] == 'AAPL' and tup[1] == 'BUY':
            total_buy_AAPL += 1
        if tup[0] == 'AAPL' and tup[1] == 'SELL':
            total_sell_AAPL += 1
        if tup[0] == 'GOOGL' and tup[1] == 'BUY':
            total_buy_GOOGL += 1
        if tup[0] == 'GOOGL' and tup[1] == 'SELL':
            total_sell_GOOGL += 1
        if tup[0] == 'MSFT' and tup[1] == 'BUY':
            total_buy_MSFT += 1
        if tup[0] == 'MSFT' and tup[1] == 'SELL':
            total_sell_MSFT += 1
        if tup[0] == 'TSLA' and tup[1] ==  'BUY':
            total_buy_TSLA += 1
        if tup[0] == 'TSLA' and tup[1] == 'SELL':
            total_sell_TSLA += 1

    curr_hold_aapl += current_prices["AAPL"] * total_buy_AAPL
    curr_hold_googl += current_prices["GOOGL"] * total_buy_GOOGL
    curr_hold_msft += current_prices["MSFT"] * total_buy_MSFT
    curr_hold_tsla += current_prices["TSLA"] * total_buy_TSLA
    print("Current Portfolio Holdings: ")
    print(f'AAPL: {curr_hold_aapl} shares')
    print(f'GOOGL: {curr_hold_googl} shares')
    print(f'MSFT: {curr_hold_msft} shares')
    print(f'TSLA: {curr_hold_tsla} shares')
    
            
def profit_loss_per_stock(transactions):
    profit_aapl = 0
    loss_aapl = 0
    profit_googl = 0
    loss_googl = 0
    profit_mstf = 0
    loss_mstf = 0
    profit_tsla = 0
    loss_tsla = 0

    sum_investment_aapl = 0
    sum_investment_googl = 0
    sum_investment_msft = 0
    sum_investment_tsla = 0
    total_investment_aapl = 0
    total_investment_googl = 0
    total_investment_msft = 0
    total_investment_tsla = 0
    aapls = 0
    googl = 0
    msft = 0
    tsla = 0
    avg_aapl = 0
    avg_googl = 0
    avg_msft = 0
    avg_tsla = 0 
    unrealized_PL_aapl = 0
    unrealized_PL_googl = 0
    unrealized_PL_msft = 0
    unrealized_PL_tsla = 0

    realiszed_PL_aapl = 0
    realiszed_PL_googl = 0
    realiszed_PL_msft = 0
    realiszed_PL_tsla = 0

    total_profit_aapl = 0
    total_profit_googl = 0
    total_profit_msft = 0
    total_profit_tsla = 0

    total_CP_aapl = 0
    total_SP_aapl = 0
    total_CP_googl = 0
    total_SP_googl = 0
    total_CP_msft = 0
    total_SP_msft = 0
    total_CP_tsla = 0
    total_SP_tsla = 0

    for tup in transactions:
        if tup[0] == 'AAPL' and tup[1] == 'BUY':
            aapls += 1
            sum_investment_aapl += tup[3]  
            avg_aapl = sum_investment_aapl / aapls 
        total_investment_aapl = aapls * avg_aapl
        unrealized_PL_aapl = (current_prices["AAPL"] - tup[3])

        if tup[0] == 'GOOGL':
            googl += 1
            sum_investment_googl += tup[3]
            avg_googl = sum_investment_googl / googl
        total_investment_googl += googl * avg_googl
        unrealized_PL_googl = (current_prices["GOOGL"] - tup[3])

        if tup[0] == 'MSFT':
            msft += 1
            sum_investment_msft += tup[3]
            avg_msft = sum_investment_msft / msft
        total_investment_msft += msft * avg_msft
        unrealized_PL_msft = (current_prices["MSFT"] - tup[3])

        if tup[0] == 'TSLA':
            tsla += 1
            sum_investment_tsla += tup[3]
            avg_tsla = sum_investment_tsla / msft
        total_investment_tsla += msft * avg_msft 
        unrealized_PL_tsla = (current_prices['TSLA'] - tup[3])


        if tup[0] == 'AAPL' and tup[1] == 'SELL':
            realiszed_PL_aapl += (current_prices["AAPL"] - tup[3])
            total_SP_aapl += tup[3]

        if tup[0] == 'AAPL' and tup[1] == 'BUY':
            total_CP_aapl += tup[3]

        total_profit_aapl = total_CP_aapl - total_SP_aapl
        
        if tup[0] == 'GOOGL' and tup[1] == 'SELL':
            realiszed_PL_googl += (current_prices["GOOGL"] - tup[3])

        
        
        if tup[0] == 'MSFT' and tup[1] == 'SELL':
            realiszed_PL_msft += (current_prices["MSFT"] - tup[3])
        
        if tup[0] == 'TSLA' and tup[1] == 'SELL':
            realiszed_PL_tsla += (current_prices["TSLA"] - tup[3])

        
        


# investment = shares owned * avg purchase price 
# realized = sales price - selling cost 
# total P & L = total CP - total SP
        
    print(f'Total invest of AAPL: {total_investment_aapl}')
    print(f'Total invest of GOOGL: {total_investment_googl}')
    print(f'total investment of MSFT: {total_investment_msft}')
    print(f'total investment of TSLa: {total_investment_tsla}')
    print(f'unrealized P & L for aapl: {unrealized_PL_aapl}') 
    print(f'unrealized P & L for googl: {unrealized_PL_googl}') 
    print(f'unrealized P & L for msft: {unrealized_PL_msft}')
    print(f'unrealized P & L for tsla: {unrealized_PL_tsla}')
    print(f'realized p & L for aapl: {realiszed_PL_aapl}')
    print(f'realized P & L for googl: {realiszed_PL_googl}')
    print(f'realized P & L for msft: {realiszed_PL_msft}')
    print(f'realized P & L for tsla: {realiszed_PL_tsla}')
    print(f'total profit price :{total_profit_aapl}')



transactions = [
("AAPL", "BUY", 100, 150.00, "2023-01-15"),
("GOOGL", "BUY", 50, 2800.00, "2023-01-20"),
("AAPL", "BUY", 50, 160.00, "2023-02-10"),
("MSFT", "BUY", 75, 300.00, "2023-02-15"),
("AAPL", "SELL", 75, 170.00, "2023-03-05"),
("GOOGL", "SELL", 20, 2900.00, "2023-03-10"),
("TSLA", "BUY", 40, 800.00, "2023-03-15"),
("MSFT", "SELL", 25, 320.00, "2023-04-01"),
("TSLA", "SELL", 15, 750.00, "2023-04-10"),
("AAPL", "BUY", 25, 155.00, "2023-04-15")
]

current_prices = {
"AAPL": 175.00,
"GOOGL": 2850.00,
"MSFT": 310.00,
"TSLA": 780.00
}

current_holdings(transactions)
profit_loss_per_stock(transactions)



