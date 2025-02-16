# starling2freeagent
Convert Starling Bank CSV format to be imported by FreeAgent 


# Motivation

I recently signed up to the Starling Bank Business account and while trying to add it to FreeAgent realised that there
are no native feeds supported, nor support for OFX or QIF which FreeAgent also supports.
The only option was CSV, but even then the format was not quite the same. The Starling CSV format has much more detail
and the column order does not match what FreeAgent supports.

After checking the CSV format that FreeAgent expects [here](https://support.freeagent.com/hc/en-us/articles/115001222564)
I wrote this basic tool to help me convert the CSV statements from Starling for direct import into FreeAgent.

## Usage

Start with a CSV statment generated by Starling Bank.
The current CSV format is this:


```
$ cat sample.csv
Date,Counter Party,Reference,Type,Amount (EUR),Balance (EUR),Spending Category,Notes
,Opening Balance,,,,0.00
09/05/2022,My Company,Transfer,SEPA PAYMENT,3132.01,3132.01,REVENUE,transfer from MyOldBank to Starling
09/05/2022,My Company,Transfer to GBP account,CURRENCY TRANSFER,-2132.01,1000.00,TRANSFERS,
```

> **Note:** Sometimes the _Opening Balance_ line is not included in the CSV. This tool automatically skips the _Opening Balance_ line if it is included in the input CSV.

Then run 

```
./s2f.py sample.csv
```


This will generate a FreeAgent version of the file with the prefix `fa-`

```
$ cat fa-sample.csv
09/05/2022,3132.01,SEPA PAYMENT: My Company [ref: Transfer] transfer from MyOldBank to Starling
09/05/2022,-2132.01,CURRENCY TRANSFER: My Company [ref: Transfer to GBP account]
```