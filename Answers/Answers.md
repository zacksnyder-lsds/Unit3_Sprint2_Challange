- In the Northwind database, what is the type of relationship between the
  `Employee` and `Territory` tables? E to T many T to E many relationship = zero or many to zero or many 

The relationship between Employee and Territory is a zero or many to one or many relationship. This is because a Territory can have a minimum of zero employees assigned to it and theoretically a maximum number of infinity employees assigned to it. On the other side of the equation, an employee can be assigned a minimum of one territory to be able to actually be an employee but has a theoretical maximum of infinite territories that can be assigned only limited by the number of territories available.  


- What is a situation where a document store (like MongoDB) is appropriate, and
  what is a situation where it is not appropriate?

  A situation where a document store database is appropriate is where vertical scaling and horizontal scaling are required. For example if you expect your application to gain 10,000 users in a night, document store databases are ideal to add large amounts of data into the databases quickly though master nodes and replicas of the master node allowing all data not to need to sit on one computer at one time. You can also horizontally scale through easy relations of one document in a document store to others in the document store. A situation where document store databases are not appropriate are when you need you're project to have ACID guarantees such as in a financial transaction application. 


- What is "NewSQL", and what is it trying to achieve?

New SQL is a form of SQL database that was built to solve the scalability issues of SQL. NewSQL is trying to maintain the ACID compliance of traditional SQL with the horizontal and vertical scalability that comes with Document Oriented Databases. This in theory would combine the best of both worlds in terms of SQL and document oriented databases that allows for an ACID compliant database that can be easily scaled. 