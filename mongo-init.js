db = db.getSiblingDB('Library');

db.createCollection('Book');
db.createCollection('Borrower')
db.createCollection('Transaction')


db.Book.insert_one({
    title: "test_title",
    author: "test_author",
    copyright: "test_copyright",
    no_pages: "test_no_pages",
    stock: "test_stock",
    updated_at: "test_updated_at"
})

/*
db.Book.insertMany([
 {
    org: 'helpdev',
    filter: 'EVENT_A',
    addrs: 'http://rest_client_1:8080/wh'
  },
  {
    org: 'helpdev',
    filter: 'EVENT_B',
    addrs: 'http://rest_client_2:8081/wh'
  },
  {
    org: 'github',
    filter: 'EVENT_C',
    addrs: 'http://rest_client_3:8082/wh'
  }
]);
*/