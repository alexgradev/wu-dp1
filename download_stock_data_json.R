# install packages if not already 

#install.packages("quantmod")
#install.packages("jsonlite")

library(quantmod)
library(jsonlite)

# download historical stock data
getSymbols("XOM", from = "1970-01-01", to = "2010-12-31", src = "yahoo")

# convert to a data frame
xom_df <- data.frame(date = index(XOM), coredata(XOM))

# rename columns for readability
colnames(xom_df) <- c("Date", "Open", "High", "Low", "Close", "Volume", "Adjusted")

# convert to JSON and save to file
xom_json <- toJSON(xom_df, pretty = TRUE)
write(xom_json, file = "xom_data.json")
