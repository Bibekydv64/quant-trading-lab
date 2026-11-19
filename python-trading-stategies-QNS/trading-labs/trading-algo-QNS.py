# # PYTHON FOR QUANT TRADING
# # VOLUME 1 — 30 DAYS / 300 EXERCISES
# # LEVEL: ABSOLUTE BEGINNER → INTERMEDIATE
# # RULE: SOLVE WITHOUT COPYING SOLUTIONS

# ==================================================
# PHASE 1 — PYTHON FOUNDATION
# DAYS 1–10 | 100 QUESTIONS
# ==================================================

# DAY 01 — VARIABLES, INPUT & OUTPUT
#---------------------------------------------------------------------------------------------------------------

# Q02. Input two prices and display their sum.

# class Stock:
#     def __init__(self):
#         pass
#     def __str__(self):
#         return('this addition Perform opeation')

#     def Stock_price(self):
#         user_stock_price1 = int(input('Enter a Price:'))
#         user_stock_price2 = int(input('Enter a price1:'))

#         sum = f'Sum of Both Prices{user_stock_price1 + user_stock_price2}'
#         return(sum)

# Stock_obj = Stock()

# print(Stock_obj.Stock_price())
#-------------------------------------------------------------------------------------------------------------------------------
# # Q03. Calculate the difference between two prices.
# class DiffrencePrices:
#     def __init__(self):
#         pass

#     def __str__(self):
#         return('This Contain diffrence of two prices:')

#     def Diffrence(self):
#         user_price1 = int(input('Enter a Number:'))
#         user_price2 = int(input("enter a Number1:"))

#         diffrence_price = (f'Price diffrence Rs:{user_price1-user_price2}')
#         return(diffrence_price)

# DiffrencePrices_obj  = DiffrencePrices()
# print(DiffrencePrices_obj.Diffrence())

#--------------------------------------------------------------------------------------------------------------------------------

# Q04. Calculate the average of three prices.
# class AvgOfThreePrice:
#     def __init__(self):
#         pass
    
#     def __str__(self):
#         return('AvgOfThreePrice')
    
#     @staticmethod
#     def avgPrice():
#         price_list = []
#         for num in range(3):
#             user_input = float(input('Enter Prices:'))
#             if user_input > 0:
#                 price_list.append(user_input)
#             else:
#                 continue

#         avg_price = (sum(price_list) / len(price_list))
#         return(f'Your Avg Price:{round(avg_price,2)}')

# print(AvgOfThreePrice.avgPrice())
# AvgOfThreePrice_obj = AvgOfThreePrice()
# print(AvgOfThreePrice_obj.avgPrice())


#-----------------------------------------------------------------------------------------------------------------------------------------

# Q06. Calculate 5% of investment capital.

# class Investement:
#     def __init__(self):
#         pass

#     def __str__(self):
#         return ('This contains of calcuate of investemt capital')

#     def invest(self):
#         user_input_capital = int(input('Enter capital:'))
#         user_input_persentage = int(input('Enter persentage of capital:'))
#         result = (user_input_capital * user_input_persentage) / 100
#         return(f'Your persentage of capital:{result}')

# Investement_obj= Investement()

# print(Investement_obj.invest())
#-----------------------------------------------------------------------------------------------------------------------------------------
# Q07. Convert NPR into USD using an exchange rate.
# Q08. Calculate profit from buying and selling.
# Q09. Calculate loss from buying and selling.
# Q10. Create a simple trading profit calculator.

# DAY 02 — COMPARISON OPERATORS

# Q11. Compare two prices and identify the higher price.
# Q12. Identify the lower price.
# Q13. Check whether two prices are equal.
# Q14. Check whether a stock price is above 100.
# Q15. Check whether a stock price is below 100.
# Q16. Check whether a price is between 100 and 200.
# Q17. Identify whether a price is positive or negative.
# Q18. Check whether trading volume exceeds 10000.
# Q19. Compare today's closing price with yesterday's.
# Q20. Create a price comparison analyzer.

# DAY 03 — IF / ELIF / ELSE

# Q21. Identify UP, DOWN or SIDEWAYS price movement.
# Q22. Identify bullish or bearish candles.
# Q23. Identify whether profit or loss occurred.
# Q24. Classify profit as small, medium or large.
# Q25. Check whether capital is sufficient for a trade.
# Q26. Identify whether price breaks above resistance.
# Q27. Identify whether price breaks below support.
# Q28. Create a basic BUY, SELL or HOLD decision.
# Q29. Check whether a trading signal meets a minimum threshold.
# Q30. Create a rule-based trading decision program.

# DAY 04 — LOGICAL OPERATORS

# Q31. Check whether price and volume both increase.
# Q32. Check whether price increases OR volume increases.
# Q33. Check whether price is not equal to the previous price.
# Q34. Detect bullish candles with high volume.
# Q35. Detect bearish candles with high volume.
# Q36. Check whether RSI is below 30 AND price is above support.
# Q37. Check whether RSI is above 70 OR price hits resistance.
# Q38. Create three conditions for a BUY signal.
# Q39. Create three conditions for a SELL signal.
# Q40. Build a multi-condition trading analyzer.

# DAY 05 — FOR LOOPS

# Q41. Print numbers from 1 to 100.
# Q42. Print stock prices from a given list.
# Q43. Count prices above 100.
# Q44. Count prices below 100.
# Q45. Count positive price changes.
# Q46. Count negative price changes.
# Q47. Calculate the sum of 10 closing prices.
# Q48. Calculate the average of 10 closing prices.
# Q49. Find the highest price in a list.
# Q50. Find the lowest price in a list.

# DAY 06 — WHILE LOOPS

# Q51. Input prices until the user enters 200.
# Q52. Count total entered prices.
# Q53. Count UP movements.
# Q54. Count DOWN movements.
# Q55. Count sideways movements.
# Q56. Calculate total upward movement.
# Q57. Calculate total downward movement.
# Q58. Track the highest price dynamically.
# Q59. Track the lowest price dynamically.
# Q60. Build an interactive price monitoring program.

# DAY 07 — COUNTERS & ACCUMULATORS

# Q61. Count bullish candles.
# Q62. Count bearish candles.
# Q63. Count candles with zero body size.
# Q64. Count consecutive bullish candles.
# Q65. Count consecutive bearish candles.
# Q66. Calculate cumulative profit.
# Q67. Calculate cumulative loss.
# Q68. Calculate total trading expenses.
# Q69. Calculate net profit after expenses.
# Q70. Build a trading performance counter.

# DAY 08 — FUNCTIONS

# Q71. Create a function to calculate profit.
# Q72. Create a function to calculate loss.
# Q73. Create a function to calculate percentage change.
# Q74. Create a function to compare two prices.
# Q75. Create a function to classify candle direction.
# Q76. Create a function to calculate candle body.
# Q77. Create a function to calculate candle range.
# Q78. Create a function to identify the highest price.
# Q79. Create a function to identify the lowest price.
# Q80. Build a reusable price analysis module.

# DAY 09 — STRINGS & TYPE CONVERSION

# Q81. Convert user input into a float.
# Q82. Validate whether a price input is numeric.
# Q83. Convert a trading signal into uppercase.
# Q84. Count characters in a trading symbol.
# Q85. Extract a symbol from a formatted string.
# Q86. Split a string containing multiple prices.
# Q87. Convert comma-separated prices into numbers.
# Q88. Format profit to two decimal places.
# Q89. Display a formatted trading report.
# Q90. Build a command-based trading interface.

# DAY 10 — MIXED PYTHON FOUNDATION

# Q91. Input 10 prices and calculate their average.
# Q92. Find the highest price without using max().
# Q93. Find the lowest price without using min().
# Q94. Count prices above their average.
# Q95. Count prices below their average.
# Q96. Identify the largest consecutive price increase.
# Q97. Identify the largest consecutive price decrease.
# Q98. Calculate total percentage change.
# Q99. Build a complete price statistics analyzer.
# Q100. Build a menu-driven trading calculator.

# ==================================================
# PHASE 2 — PYTHON LOGIC BUILDING
# DAYS 11–20 | 100 QUESTIONS
# ==================================================

# DAY 11 — LISTS

# Q101. Store 10 stock prices in a list.
# Q102. Append a new price.
# Q103. Remove a price from a list.
# Q104. Update a particular price.
# Q105. Access the first and last prices.
# Q106. Find the second-highest price without sort().
# Q107. Count duplicate prices.
# Q108. Reverse a price list without reverse().
# Q109. Separate positive and negative price changes.
# Q110. Build a price-list management program.

# DAY 12 — LIST LOGIC

# Q111. Find all prices above 100.
# Q112. Find all prices below 100.
# Q113. Separate bullish and bearish price changes.
# Q114. Calculate the difference between adjacent prices.
# Q115. Generate a list of percentage changes.
# Q116. Find consecutive duplicate prices.
# Q117. Find the longest increasing sequence.
# Q118. Find the longest decreasing sequence.
# Q119. Remove duplicate prices while preserving order.
# Q120. Build a price movement analyzer using lists.

# DAY 13 — NESTED LOOPS & CONDITIONS

# Q121. Compare every price with every other price.
# Q122. Find all pairs whose sum equals 200.
# Q123. Identify duplicate prices using nested loops.
# Q124. Compare today's prices against previous prices.
# Q125. Find all consecutive upward movements.
# Q126. Find all consecutive downward movements.
# Q127. Detect three consecutive bullish candles.
# Q128. Detect three consecutive bearish candles.
# Q129. Find repeated price patterns.
# Q130. Build a basic pattern detection program.

# DAY 14 — DICTIONARIES

# Q131. Store OHLC values in a dictionary.
# Q132. Access Open, High, Low and Close.
# Q133. Update the closing price.
# Q134. Add trading volume.
# Q135. Calculate candle body using dictionary values.
# Q136. Calculate candle range.
# Q137. Store multiple stocks and their prices.
# Q138. Find the highest-priced stock.
# Q139. Find the lowest-priced stock.
# Q140. Build a stock information manager.

# DAY 15 — LISTS OF DICTIONARIES

# Q141. Store 10 candles as dictionaries.
# Q142. Print every candle's closing price.
# Q143. Count bullish candles.
# Q144. Count bearish candles.
# Q145. Find the candle with the highest high.
# Q146. Find the candle with the lowest low.
# Q147. Calculate average candle body size.
# Q148. Identify candles with unusually large ranges.
# Q149. Calculate average trading volume.
# Q150. Build a basic OHLCV analyzer.

# DAY 16 — FUNCTIONS & REUSABILITY

# Q151. Create an OHLC candle classification function.
# Q152. Create a percentage return function.
# Q153. Create a moving average function.
# Q154. Create a maximum drawdown function.
# Q155. Create a position sizing function.
# Q156. Create a stop-loss calculation function.
# Q157. Create a risk-to-reward function.
# Q158. Create a win-rate function.
# Q159. Combine multiple functions into one analyzer.
# Q160. Build a reusable trading utilities library.

# DAY 17 — ADVANCED LOOP LOGIC

# Q161. Find the longest bullish streak.
# Q162. Find the longest bearish streak.
# Q163. Find the longest sideways streak.
# Q164. Detect three rising closing prices.
# Q165. Detect five falling closing prices.
# Q166. Find the maximum consecutive upward movement.
# Q167. Find the maximum consecutive downward movement.
# Q168. Count trend changes.
# Q169. Identify alternating UP and DOWN movements.
# Q170. Build a market behavior analyzer.

# DAY 18 — TUPLES, SETS & DATA STRUCTURES

# Q171. Store fixed OHLC values in a tuple.
# Q172. Unpack OHLC values into variables.
# Q173. Store unique trading symbols in a set.
# Q174. Find common symbols between two watchlists.
# Q175. Find symbols that appear in only one watchlist.
# Q176. Remove duplicate trading signals.
# Q177. Count unique closing prices.
# Q178. Compare two portfolios using sets.
# Q179. Store immutable configuration values.
# Q180. Build a watchlist manager.

# DAY 19 — EXCEPTION HANDLING & VALIDATION

# Q181. Handle non-numeric price input.
# Q182. Prevent division by zero.
# Q183. Reject negative stock prices.
# Q184. Validate OHLC price relationships.
# Q185. Validate that High is not below Open or Close.
# Q186. Validate that Low is not above Open or Close.
# Q187. Handle empty price lists.
# Q188. Handle missing trading data.
# Q189. Validate trading capital before placing a simulated trade.
# Q190. Build a robust input validation system.

# DAY 20 — MIXED LOGIC CHALLENGE

# Q191. Build a multi-stock price tracker.
# Q192. Build a candle statistics analyzer.
# Q193. Build a trend streak detector.
# Q194. Build a percentage return calculator.
# Q195. Build a basic portfolio tracker.
# Q196. Build a trade history manager.
# Q197. Build a profit/loss report generator.
# Q198. Build a price alert system.
# Q199. Build a multi-condition signal generator.
# Q200. Build a command-line trading dashboard.

# ==================================================
# PHASE 3 — PRICE ACTION & CANDLE ANALYSIS
# DAYS 21–30 | 100 QUESTIONS
# ==================================================

# DAY 21 — CANDLESTICK MATHEMATICS

# Q201. Calculate candle body size.
# Q202. Calculate upper wick size.
# Q203. Calculate lower wick size.
# Q204. Calculate total candle range.
# Q205. Calculate body-to-range percentage.
# Q206. Calculate upper wick-to-range percentage.
# Q207. Calculate lower wick-to-range percentage.
# Q208. Classify strong bullish candles.
# Q209. Classify strong bearish candles.
# Q210. Build a candlestick measurement engine.

# DAY 22 — CANDLE PATTERNS

# Q211. Detect a doji candle using a defined body threshold.
# Q212. Detect a hammer-like candle.
# Q213. Detect a shooting-star-like candle.
# Q214. Detect a bullish engulfing pattern.
# Q215. Detect a bearish engulfing pattern.
# Q216. Detect a bullish harami pattern.
# Q217. Detect a bearish harami pattern.
# Q218. Detect an inside bar.
# Q219. Detect an outside bar.
# Q220. Build a rule-based candlestick pattern detector.

# DAY 23 — PRICE TRENDS

# Q221. Identify an upward price sequence.
# Q222. Identify a downward price sequence.
# Q223. Detect a sequence of higher closing prices.
# Q224. Detect a sequence of lower closing prices.
# Q225. Count trend continuation movements.
# Q226. Count trend reversals.
# Q227. Identify consolidation using a defined price range.
# Q228. Calculate trend duration.
# Q229. Calculate percentage trend strength.
# Q230. Build a basic trend detection engine.

# DAY 24 — SUPPORT & RESISTANCE

# Q231. Identify local price highs.
# Q232. Identify local price lows.
# Q233. Find repeated price rejection levels.
# Q234. Count touches near a resistance level.
# Q235. Count touches near a support level.
# Q236. Identify a support breakout.
# Q237. Identify a resistance breakout.
# Q238. Calculate breakout percentage.
# Q239. Detect a failed breakout using subsequent prices.
# Q240. Build a rule-based support/resistance analyzer.

# DAY 25 — MARKET STRUCTURE

# Q241. Identify Higher High (HH).
# Q242. Identify Higher Low (HL).
# Q243. Identify Lower High (LH).
# Q244. Identify Lower Low (LL).
# Q245. Detect bullish market structure.
# Q246. Detect bearish market structure.
# Q247. Identify a potential Break of Structure (BOS).
# Q248. Identify a potential Change of Character (CHOCH).
# Q249. Detect a structural trend reversal.
# Q250. Build a market structure analyzer using defined swing points.

# DAY 26 — VOLUME ANALYSIS

# Q251. Find average trading volume.
# Q252. Detect above-average volume.
# Q253. Detect below-average volume.
# Q254. Compare current volume with previous volume.
# Q255. Detect rising volume during rising prices.
# Q256. Detect rising volume during falling prices.
# Q257. Calculate volume change percentage.
# Q258. Identify volume spikes using a threshold.
# Q259. Confirm a breakout with volume.
# Q260. Build a price-volume analyzer.

# DAY 27 — MOMENTUM ANALYSIS

# Q261. Calculate momentum over one period.
# Q262. Calculate momentum over five periods.
# Q263. Calculate rate of change (ROC).
# Q264. Identify accelerating upward movement.
# Q265. Identify decelerating upward movement.
# Q266. Identify accelerating downward movement.
# Q267. Identify weakening downward momentum.
# Q268. Compare price momentum with volume.
# Q269. Detect a possible momentum reversal.
# Q270. Build a momentum analysis engine.

# DAY 28 — DEMAND & SUPPLY LOGIC

# Q271. Identify a strong upward departure from a price base.
# Q272. Identify a strong downward departure from a price base.
# Q273. Define a demand zone using swing structure.
# Q274. Define a supply zone using swing structure.
# Q275. Calculate zone width.
# Q276. Count zone retests.
# Q277. Detect a zone breakout.
# Q278. Calculate distance between price and zone.
# Q279. Create a rule-based zone invalidation condition.
# Q280. Build a demand/supply zone analyzer.

# DAY 29 — MULTI-CONDITION PRICE ACTION

# Q281. Detect bullish structure with bullish candle confirmation.
# Q282. Detect bearish structure with bearish candle confirmation.
# Q283. Detect support breakout with volume confirmation.
# Q284. Detect resistance breakout with volume confirmation.
# Q285. Detect demand-zone reaction.
# Q286. Detect supply-zone reaction.
# Q287. Combine trend and momentum conditions.
# Q288. Combine structure and volume conditions.
# Q289. Build a multi-condition BUY/SELL/HOLD system.
# Q290. Test the system on manually supplied price sequences.

# DAY 30 — FINAL BEGINNER-TO-INTERMEDIATE PROJECTS

# Q291. Build a complete candle analyzer.
# Q292. Build a market trend analyzer.
# Q293. Build a support/resistance detector.
# Q294. Build a market structure detector.
# Q295. Build a price and volume analyzer.
# Q296. Build a demand/supply zone tracker.
# Q297. Build a multi-condition signal generator.
# Q298. Build a trading journal using Python dictionaries and lists.
# Q299. Build a market analysis command-line dashboard.
# Q300. Build a complete rule-based price action analysis program.

# ==================================================
# DAILY PRACTICE RULES
# ==================================================

# 1. Solve 10 questions per day.
# 2. First understand the problem.
# 3. Write pseudocode before Python when needed.
# 4. Write your own code.
# 5. Test at least three different inputs.
# 6. Test boundary conditions and invalid inputs.
# 7. Explain why your logic works.
# 8. Refactor repeated code into functions.
# 9. Never copy solutions before attempting the problem.
# 10. Review mistakes and solve them again.

# ==================================================
# IMPORTANT TRAINING PRINCIPLES
# ==================================================

# - No pandas before mastering basic Python collections.
# - No NumPy before understanding basic calculations.
# - No ML before establishing a reliable baseline.
# - No strategy deployment before backtesting.
# - No profitability claims without statistical evidence.
# - Include spread, fees and slippage in strategy testing.
# - Avoid look-ahead bias and data leakage.

# ==================================================
# COMPLETION TARGET
# ==================================================

# After these 30 days, you should be able to:

# 1. Process sequences of prices.
# 2. Analyze OHLC candles.
# 3. Build basic market structure rules.
# 4. Create reusable Python functions.
# 5. Build rule-based market analyzers.
# 6. Convert observations into testable conditions.

# NEXT VOLUME:
# Days 31–60 — Risk Management, Technical Indicators,
# Strategy Development and Backtesting.

# FINAL DESTINATION:
# Independent Quantitative Trading System Developer.
