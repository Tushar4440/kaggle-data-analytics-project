use project;

select * from dbo.orders_data;

--Q1 write a sql query to list all distinct cities where orders have been shipped.
select distinct City from orders_data;

--Q2 Calculate total selling price and profits of all orders.
select [Order Id], sum(Quantity * Unit_Selling_Price) as 'Total_Selling_Price',
cast(sum(Quantity * Unit_Profit) as decimal(10,2)) as 'Total Profit'
from orders_data group by [Order Id] order by [Total Profit] desc

--Q3 Write a query to find all orders from the 'Technology' category that were shipped using 
-- 'Second class' ship mode, ordered by 'order date'.
select [Order Id], Category, [Ship Mode], [Order Date]
from orders_data
where Category = 'Technology' and [Ship Mode]='Second Class'
order by [Order Date];

--Q4 Write Average Order Value
select cast(avg(Quantity*Unit_Selling_Price) as decimal(10,2)) as AOV from orders_data

--Q5 Select city with the highest total quantity of products ordered.
select top 1 City, sum(Quantity) as 'Total Quantity' from orders_data
group by City order by [Total Quantity] desc

--Q6 Use window function to rank orders in each region by quantity in descending order.
select [Order Id], Region, Quantity as 'Total_Quantity',
DENSE_RANK() over (partition by region order by Quantity desc) as rnk
from orders_data 
order by Region,rnk

--Q7 Write sql query to list all the orders placed in the first quarter of any year (jan to mar),
-- including the total cost for these orders.

select [Order Id], sum(Quantity * Unit_Selling_Price) as 'total value' from orders_data
where month([Order Date]) in (1,2,3) group by [Order Id] order by [total value] desc

--Q8 Find top 10 highest profit generating products
select top 10 [Product Id], sum([Total Profit]) as 'Total profit' from orders_data
group by [Product Id] order by [Total profit] desc

--alternate above quesiton answer using window function
with cte as(
	select [Product Id], sum([Total Profit]) as profit, dense_rank() over (order by sum([Total Profit]) desc) as rn
	from orders_data group by [Product Id]
)
select [Product Id], Profit from cte where rn <= 10;

--Q9 top 3 highest selling products in each region
with cte as (
	select Region,[Product Id], sum(Quantity * Unit_Selling_Price) as Total_Sales, 
	Dense_rank() over(partition by Region order by sum(Quantity*Unit_Selling_Price) desc) as rn
	from orders_data	
	group by Region, [Product Id]
)
select * from cte where rn <= 3

--Q10 Find month over month growth comparison for 2022 and 2023 eg: jan 2022 vs jan 2023
with cte as(
	select YEAR([Order Date]) as order_year, MONTH([Order Date]) as order_month,
	sum(Quantity * Unit_Selling_Price) as sales
	from orders_data
	group by year([Order Date]), month([Order Date])
)
select order_month,
round(sum(case when order_year=2022 then sales else 0 end),2) as growth_2022_sale,
round(sum(case when order_year=2023 then sales else 0 end),2) as growth_2023_sale,
round(((round(sum(case when order_year=2022 then sales else 0 end),2) - round(sum(case when order_year=2023 then sales else 0 end),2)) / round(sum(case when order_year=2022 then sales else 0 end),2) * 100),2) as comparison
from cte
group by order_month order by order_month

--Q11 For each category which month has the highest sales
with cte as(
	select Category, format([Order Date], 'yyyy-MM') as order_year_month, 
	sum(Quantity * Unit_Selling_Price) as sales,
	DENSE_RANK() over (partition by Category order by sum(Quantity * Unit_Selling_Price) desc) as rn
	from orders_data
	group by Category, format([Order Date], 'yyyy-MM')
)
select Category , order_year_month as 'Order_Year_Month', sales as 'Total Sales'
from cte where rn = 1