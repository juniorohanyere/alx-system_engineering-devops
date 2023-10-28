# Simple Web Stack

A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a LAMP stack.

This is a design of a `one server` web infrastructure that hosts a website that is reachable via www.foobar.com. This explanation begins by having a user wanting to access the website.

## Some Specifics About This Infrastructure

**Infrastructure Design:**

1. **Server (8.8.8.8):** This is a physical or virtual machine responsible for hosting the entire web application. It runs the Linux operating system.

2. **Domain Name (www.foobar.com):** The domain name is a human-readable address that users use to access the website. It's configured with a DNS "A" record pointing to the server's IP address (8.8.8.8). This mapping allows users' devices to locate the server.

3. **Web Server (Nginx):** Nginx is the web server software responsible for handling incoming HTTP requests from users. It listens for requests on port 80 and routes them to the appropriate resources. Its role is to serve static content, handle SSL/TLS encryption, and manage load balancing if needed.

4. **Application Server:** This component runs the web application's server-side logic. It can be a component like PHP-FPM, Gunicorn for Python, or a similar technology. The application server executes dynamic code and communicates with the database.

5. **Application Files (Code Base):** These are the files and scripts that make up the web application, including HTML, CSS, JavaScript, and server-side code like PHP, Python, or Perl. The application server executes these files.

6. **Database (MySQL):** The database stores and manages the application's data. It handles queries, storage, and retrieval of information. In this case, MySQL is used, but other databases like PostgreSQL, SQLite, or NoSQL databases can be chosen based on specific requirements.

**Explanation of Specifics:**

- **What is a Server:** A server is a computer or software system that provides services, data, or resources to other computers or devices over a network, such as the internet. In this context, it hosts the web application.

- **Role of the Domain Name:** The domain name (www.foobar.com) provides a human-friendly way to access the website, acting as a pointer to the server's IP address.

- **Type of DNS Record "www" is in www.foobar.com:** The "www" in www.foobar.com is a subdomain. It's typically configured as a CNAME (Canonical Name) or A (Address) record in the DNS, pointing to the server's IP address.

- **Role of the Web Server:** Nginx serves as the entry point for incoming HTTP requests. It handles SSL/TLS encryption, manages routing, and can load balance traffic if necessary.

- **Role of the Application Server:** The application server executes dynamic code, interacts with the database, and generates dynamic content for users.

- **Role of the Database:** The database stores, retrieves, and manages the web application's data. It is essential for dynamic web applications that rely on user-specific information.

- **Server Communication with User's Computer:** The server communicates with the user's computer over the internet using the HTTP/HTTPS protocol. When a user requests www.foobar.com, the server sends the web page content and other resources as HTTP responses.

**Issues with the Infrastructure:**

1. **Single Point of Failure (SPOF):** This infrastructure has a single server. If it fails, the entire website becomes unavailable. To address this, you can introduce redundancy by adding backup servers and load balancing.

2. **Downtime during Maintenance:** When performing maintenance or deploying new code, the web server often needs to be restarted. This can result in temporary downtime for the website. To mitigate this, a load balancer and multiple application server instances can be used to ensure continuous service.

3. **Limited Scalability:** With only one server, the infrastructure cannot handle a significant increase in incoming traffic. Horizontal scaling, adding more servers and load balancing, is required to handle increased traffic efficiently.
