# data-enrichment

Create a Github repo called ‘data-enrichment’ in your account, and write python code that will enrich SPARCS.csv with
public health information from the Neighborhood Atlas and if you want to, but not manditory, you can choose another dataset of your choice

For the Neighborhood Atlas, go to: https://www.neighborhoodatlas.medicine.wisc.edu/ register and go to ‘download data’ section on top right-hand side of screen

For the Hospital Inpatient Discharges (SPARCS) data (.csv), please go to https://health.data.ny.gov/Health/Hospital-Inpatient-Discharges-SPARCS-De-Identified/82xm-y6g8 and download the .csv file from the EXPORT -> CSV for Excel format. This is the 2015 NYDOH Hospital Inpatient Discharges (SPARCS de-identified) 2015 information.  

The data that you decide to enrich with, should be based/linked to either a zipcode, county, city, or state level to the SPARCS.csv

# Errors

One of the primary errors I obtained was attempting to push repo. I found out that I cannot push more than 100 mb of information. In order to resolve this I had added the csv files in .gitignore so I am able to push

I had a lot of trouble trying to merge the data. After reading the code, I kept outputting nan or an empty space when I merged the code. I have tried multiple reseources to remedy this but I was not able to find a solution for myself.

difficult to run line 26 without killing the script

tried concat to see if i can remove nan in zipid values