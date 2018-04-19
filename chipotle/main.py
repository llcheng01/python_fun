import csv

def main():
    orders = {}
    with open('chipotle.tsv') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        next(reader)    # skip header
        parser = Parser();
        order_id = row[0]
        order = orders.get(order_id, [])
        for row in reader:
            item = parser.parse(row)
            # (quantity, item)
            order.append((row[1], item)

if __name__ == '__main__':
    main()
