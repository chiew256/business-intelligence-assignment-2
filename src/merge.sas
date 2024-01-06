FILENAME REFFILE1 '/home/u63723139/bai/DataSources/cleaned_FAOSTAT_data_en_12-28-2023.csv';
FILENAME REFFILE2 '/home/u63723139/bai/DataSources/cleaned_GCB2023v28_MtCO2_flat.csv';

PROC IMPORT DATAFILE=REFFILE1
    DBMS=CSV
    OUT=WORK.FAOSTAT;
    GETNAMES=YES;
RUN;

PROC IMPORT DATAFILE=REFFILE2
    DBMS=CSV
    OUT=WORK.CO2;
    GETNAMES=YES;
RUN;

data merged_data;
    merge WORK.FAOSTAT (in=a) WORK.CO2 (in=b);
    by Country Year;
    if a and b;
run;

PROC EXPORT DATA=WORK.merged_data
    OUTFILE='/home/u63723139/bai/DataSources/merged.csv'
    DBMS=CSV
    REPLACE;
RUN;