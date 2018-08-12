--Compute the current date.
    SELECT date('now');

--Compute the last day of the current month.
    SELECT date('now','start of month','+1 month','-1 day');

--Compute the date and time given a unix timestamp 1092941466.
    SELECT datetime(1092941466, 'unixepoch');

--Compute the date and time given a unix timestamp 1092941466, and compensate for your local timezone.
    SELECT datetime(1092941466, 'unixepoch', 'localtime');

--Compute the current unix timestamp.
    SELECT strftime('%s','now');

--Compute the number of days since the signing of the US Declaration of Independence.
    SELECT julianday('now') - julianday('1776-07-04');

--Compute the number of seconds since a particular moment in 2004:
    SELECT strftime('%s','now') - strftime('%s','2004-01-01 02:34:56');

--Compute the date of the first Tuesday in October for the current year.
    SELECT date('now','start of year','+9 months','weekday 2');

--Compute the time since the unix epoch in seconds (like strftime('%s','now') except includes fractional part):
    SELECT (julianday('now') - 2440587.5)*86400.0;
