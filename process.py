import pandas as pd


def join_data():
    orders = pd.read_csv('/tmp/orders/data-00000')
    customers = pd.read_csv('/tmp/customers/data-00000')
    order_count_by_customer = customers. \
        join(orders.set_index('order_customer_id'),
             on='customer_id',
             how='inner'
            ). \
        groupby('customer_id')['customer_id']. \
        agg(['count']). \
        rename(columns={'count': 'order_count'})
    order_count_by_customer.to_csv('/tmp/join_orders_and_customers/data-00000')
    return


if __name__ == '__main__':
    join_data()