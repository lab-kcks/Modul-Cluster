<img
style="margin: 0 auto; width: 100%"
src="https://www.dicoding.com/blog/wp-content/uploads/2020/05/web-service.jpg">

# Definisi
Web Service adalah sebuah aplikasi berbasis client-server yang dapat digunakan untuk menjembatani banyak aplikasi untuk saling berkomunikasi satu sama lain tanpa dibatasi oleh bahasa pemrograman tertentu. Dalam Web Service, sebuah teknologi web seperti HTTP digunakan untuk mengirimkan file dengan format machine-readable seperti XML dan JSON.

Secara singkat, Web Service dapat didefinisikan sebagai berikut:
- Merupakan aplikasi client-server atau komponen aplikasi untuk komunikasi.
- Client mengirimkan request ke server (service), dan service mengirimkan response ke client.
- Kumpulan standar atau protokol untuk bertukar informasi antara dua perangkat atau aplikasi.

https://www.cleo.com/blog/knowledge-base-web-services

<img
style="margin: 0 auto; width: 100%"
src="https://static.javatpoint.com/webservicepages/images/web-services.png">

# Jenis
### XML-RPC (Remote Procedure Call)
Protokol XML paling dasar untuk bertukar data antara berbagai perangkat di jaringan. XML-RPC menggunakan HTTP untuk dapat dengan cepat dan mudah berkomunikasi  dari klien ke server dan sebaliknya.

### SOAP (Simple Object Access Protocol)
Protokol layanan Web berbasis XML untuk bertukar data dan dokumen melalui HTTP atau SMTP (Simple Mail Transfer Protocol). Ini memungkinkan proses yang beroperasi pada sistem yang berbeda untuk berkomunikasi menggunakan XML.

### REST (Representational State Transfer)
Menyediakan komunikasi dan konektivitas antara perangkat dan internet berbasis API. Sebagian besar layanan RESTful menggunakan HTTP sebagai protokol pendukungnya.

Dalam HTTP terdapat berbagai method yang dapat digunakan, contohnya:

| HTTP Method | CRUD                  | Collection Resource (e.g. /users)                                                                       | Single Resouce (e.g. /users/123)                                                 |
| --------    | ---                   | ---                                                                                                     | ---                                                                              |
| POST        | Create                | 201 (Created), ‘Location’ header with link to /users/{id} containing new ID                             | Avoid using POST on a single resource                                            |
| GET         | Read                  | 200 (OK), list of users. Use pagination, sorting, and filtering to navigate big lists                   | 200 (OK), single user. 404 (Not Found), if ID not found or invalid               |
| PUT         | Update/Replace        | 405 (Method not allowed), unless you want to update every resource in the entire collection of resource | 200 (OK) or 204 (No Content). Use 404 (Not Found), if ID is not found or invalid |
| PATCH       | Partial Update/Modify | 405 (Method not allowed), unless you want to modify the collection itself                               | 200 (OK) or 204 (No Content). Use 404 (Not Found), if ID is not found or invalid |
| DELETE      | Delete                | 405 (Method not allowed), unless you want to delete the whole collection — use with caution             | 200 (OK). 404 (Not Found), if ID not found or invalid                            |

[Sumber](https://restfulapi.net/http-methods/)

Untuk list lebih lengkap mengenai framework dan protocol Web Service dapat dilihat di:
- Framework https://en.wikipedia.org/wiki/List_of_web_service_frameworks
- Protokol https://en.wikipedia.org/wiki/List_of_web_service_protocols

# Menghubungkan dengan database (Web Service)

Salah satu fitur dari Web Service ini yaitu dapat ditulis dari berbagai bahasa pemrograman, bahkan sudah banyak framework yang dapat digunakan untuk membuat Web Service.

Pada contoh kali ini akan digunakan contoh REST API yang berisi list bahasa pemrograman dan ranking-nya dari GitHut, PYPL, dan TIOBE index. ([Sample Web Service](https://blog.logrocket.com/node-js-express-js-mysql-rest-api-example/))

Untuk mempermudah interaksi dengan REST API ini kita gunakan [Postman](https://www.getpostman.com/).

Berikut adalah data dalam database:
![database](https://gcdn.pbrd.co/images/g1YytRBADMAv.png?o=1)

Kita dapat menguji koneksi dengan service dengan cara melakukan `GET` request ke endpoint `/programming-languages`. Server akan mengirimkan response berupa data dalam format `JSON`:
![response-get](https://gcdn.pbrd.co/images/cCFRGVJ9Vc9W.png?o=1)

# Mengirimkan dan menerima data dari database

Selain dapat meminta data dari database, kita juga dapat mengirimkan data ke database. Data dikirimkan dalam format `JSON` umumnya menggunakan method `POST`.

Contoh membuat data baru dengan entry bahasa pemrograman `dart` beserta ranking-nya.
![create](https://gcdn.pbrd.co/images/KbIAj7obP9rk.png?o=1)

Server akan menerima data dari client dan menyimpannya di database dan mengirimkan response kembali:
![response-create](https://gcdn.pbrd.co/images/9YwKULMycOhN.png?o=1)

Pada database data tersebut juga sudah tersimpan:
![database-create](https://gcdn.pbrd.co/images/dztqKvC8UTmd.png?o=1)

# Praktik Sederhana hasil Query upload data/download data otomatis


# Sumber:
https://www.dicoding.com/blog/apa-itu-web-service/
https://www.guru99.com/web-service-architecture.html
https://www.javatpoint.com/what-is-web-service
https://en.wikipedia.org/wiki/Web_service
https://www.cleo.com/blog/knowledge-base-web-services
https://www.mysqltutorial.org/mysql-sample-database.aspx
