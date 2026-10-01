# Write your MySQL query statement below
with cal_data as (
    select
        visited_on,
        sum(amount) as tt_sum,
        row_number() over(order by visited_on) as rn
    from Customer
    group by visited_on
),
sum_avg as (
    select 
        *,
        sum(tt_sum) over(order by visited_on rows between 6 preceding and current row) as amount,
        round(Avg(tt_sum) over(order by visited_on rows between 6 preceding and current row),2) as average_amount
    from cal_data
)

select 
    visited_on,
    amount,
    average_amount
from sum_avg
where rn>6;
