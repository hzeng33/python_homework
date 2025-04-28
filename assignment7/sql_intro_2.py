# Task 6: Read Data into a DataFrame
import sqlite3
import pandas as pd


with sqlite3.connect("../db/lesson.db") as conn:
    sql = """
        SELECT li.line_item_id,
            li.quantity,
            li.product_id,
            p.product_name,
            p.price
        FROM line_items AS li
        JOIN products AS p
        ON li.product_id = p.product_id;
    """
    
    df = pd.read_sql_query(sql, conn)
    print("First 5 lines of the resulting DataFrame:\n", df.head(5))

    # Add a column to the DataFrame called "total".
    df['total'] = df['quantity'] * df['price']
    print("First 5 lines of DataFrame with total column: \n", df.head(5))
    
    # Group by product_id
    df = df.groupby('product_id').agg({
          'line_item_id': 'count',
          'total':        'sum',
          'product_name':'first'
      }).rename(columns={
          'line_item_id':'order_count',
          'total':'total_revenue'
      })
    print("First 5 lines of DataFrame after group be product_id:\n", df.head(5))
    
    #Sort the DataFrame by the product_name column
    df = df.sort_values(by='product_name')
    
    # write this DataFrame to a file order_summary.csv
    df.to_csv('order_summary.csv')
    print("Successfully written to file order_summary.csv")