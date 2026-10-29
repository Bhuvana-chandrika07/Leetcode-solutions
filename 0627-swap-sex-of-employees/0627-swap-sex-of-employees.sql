UPDATE Salary
SET sex = 
CASE 
    when sex = 'm' then 'f'
    else 'm'
end