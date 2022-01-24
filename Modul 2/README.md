# Pengenalan Web Service
Web Service adalah sebuah aplikasi berbasis **client-server** atau **consumer-provider** yang dapat digunakan untuk menjembatani banyak aplikasi untuk saling **berkomunikasi** satu sama lain __tanpa dibatasi oleh bahasa pemrograman__ tertentu. Dalam Web Service, sebuah *teknologi web* seperti **HTTP** digunakan untuk mengirimkan file dengan format machine-readable seperti **XML** atau **JSON**.

Secara singkat, Web Service dapat didefinisikan sebagai berikut:
- Sebuah layanan yang tersedia melalui internet
- Merupakan aplikasi client-server atau komponen aplikasi untuk komunikasi.
- Client mengirimkan request ke server (service), dan service mengirimkan response ke client.
- Kumpulan standar atau protokol untuk bertukar informasi antara dua perangkat atau aplikasi.

https://www.cleo.com/blog/knowledge-base-web-services

<img
style="margin: 0 auto; width: 100%"
src="https://static.javatpoint.com/webservicepages/images/web-services.png">

Gambar diatas menunjukkan bagaimana aplikasi-aplikasi yang ditulis dengan berbagai bahasa dapat **saling berinteraksi** antar satu sama lain ataupun dengan Web Service itu sendiri. Interaksi ini dapat berupa permintaan data, mengirimkan notifikasi, atau mengeksekusi instruksi dari aplikasi tersebut.

# Jenis
https://www.studytonight.com/rest-web-service/types-of-webservices
## XML-RPC (Remote Procedure Call)
Protokol XML paling dasar untuk bertukar data antara berbagai perangkat di jaringan. XML-RPC menggunakan HTTP untuk dapat dengan cepat dan mudah berkomunikasi  dari klien ke server dan sebaliknya. Dalam XML-RPC interaksi ini dilakukan dengan mengirim **dokumen xml** yang didalamnya berisi **metode dan parameter dari permintaan yang diinginkan**.

Seperti namanya XML-RPC memanfaatkan komunikasi **RPC** (Remote Procedure Call) dimana satu komputer dapat membuat komputer lain mengeksekusi sebuah fungsi/subroutine seakan akan dilakukan oleh komputer lain tersebut. Berbeda dengan **IPC** (Inter-process communication) dimana sebuah proses berkomunikasi dengan process lain **didalam komputer/host machine yang sama**.

**Contoh Request XML-RPC**:
```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>examples.getStateName</methodName>
  <params>
    <param>
        <value><i4>40</i4></value>
    </param>
  </params>
</methodCall>
```

Dapat dilihat dalam contoh request tersebut terdapat tag `<methodCall>` yang memberikan informasi bahwa didalam tag tersebut akan ada nama *method* yang ingin dipanggil dan *parameter* apa saja yang diberikan. Dalam tag `<methodName>` ada nama method yang ingin dipanggil. Method ini sendiri dapat berupa *fungsi/function* dalam pemrograman yang bertugas untuk melakukan intruksi-intruksi tertentu. Dalam tag `<params>` berisi *parameter* yang diberikan, parameter ini dapat dianggap seperti argumen dalam yang akan digunakan dalam *function* yang dipanggil pada `<methodName>`.

**Contoh Response XML-RPC**:
```xml
<?xml version="1.0"?>
<methodResponse>
  <params>
    <param>
        <value><string>South Dakota</string></value>
    </param>
  </params>
</methodResponse>
```

Ketika request dari client ini **berhasil diproses** oleh server, server akan mengirimkan kembali response dari request yang diberikan tadi sesuai dengan *method* dan *parameter* yang diberikan. Dalam contoh request tadi client mengirimkan request untuk meminta data **negara bagian** (state) dengan id `40` (dilihat dari parameter request), maka server memberikan response berupa string yang berisi `South Dakota`. Client akan menerima response yang dikirim oleh server ini.

**Contoh Fault/Error Response XML-RPC**:
```xml
<?xml version="1.0"?>
<methodResponse>
  <fault>
    <value>
      <struct>
        <member>
          <name>faultCode</name>
          <value><int>4</int></value>
        </member>
        <member>
          <name>faultString</name>
          <value><string>Too many parameters.</string></value>
        </member>
      </struct>
    </value>
  </fault>
</methodResponse>
```

Tentu saja akan ada kemungkinan client mengirimkan **request yang tidak sesuai**, kadang melakukan request pada data yang tidak tersedia, atau request yang dikirim tidak memiliki struktur yang benar. Server harus tetap dapat menangani request ini, proses ini disebut sebagai **Error Handling**, dalam kasus ini **client mengirimkan request dengan parameter berlebih** sehingga server tidak dapat memroses data tersebut. Server akan mengirimkan sebuah *Error Message* yang sesuai sehingga client dapat mengetahui error tersebut.

### Tag tipe data (data-type) dalam XML-RPC
- **Array**

```xml
<array>
  <data>
    <value><i4>1404</i4></value>
    <value><string>Something here</string></value>
    <value><i4>1</i4></value>
  </data>
</array>
```

> *Array of values*, tidak menyimpan `key`

- **Base64**
```xml
<base64>eW91IGNhbid0IHJlYWQgdGhpcyE=</base64>
```
> Data biner yang *di-encode* Base64

- **Boolean**
```xml
<boolean>1</boolean>
```
> Boolean logical value (0 atau 1)

- **Date/Time**
```xml
<dateTime.iso8601>19980717T14:08:55Z</dateTime.iso8601>
```
> Date and time in ISO 8601 format

- **Double**
```xml
<double>-12.53</double>
```
> Angka floating point presisi double

- **Integer**
```xml
<int>42</int>
```
> Atau

```xml
<i4>42</i4>
```
> Bilangan bulat, integer.

- **String**
```xml
<string>Hello world!</string>
```
> atau

```xml
Hello world!
```
> Rangkaian karakter. Harus mengikuti *encoding* XML.

- **Struct**
```xml
<struct>
  <member>
    <name>foo</name>
    <value><i4>1</i4></value>
  </member>
  <member>
    <name>bar</name>
    <value><i4>2</i4></value>
  </member>
</struct>
```
> Associative array

- **nil**
```xml
<nil/>
```

> Nilai nil; ekstensi XML-RPC

<br><br>


### SOAP (Simple Object Access Protocol)
Protokol layanan Web berbasis XML untuk bertukar data dan dokumen melalui HTTP atau SMTP (Simple Mail Transfer Protocol). Ini memungkinkan proses yang beroperasi pada sistem yang berbeda untuk berkomunikasi menggunakan XML.

### REST (Representational State Transfer)
Menyediakan komunikasi dan konektivitas antara perangkat dan internet berbasis API. Sebagian besar layanan RESTful menggunakan HTTP sebagai protokol pendukungnya.

# Bagaimana Web Service Bekerja
Salah satu cara Web Service berinteraksi yaitu melalui protokol HTTP/HTTPS, Ada satu atau sekumpulan komputer yang bertindak sebagai client yang akan mengirimkan permintaan (request) kepada server dengan method-method (**HTTP Methods**) yang ada dan server akan mengirimkan data kembali (response) kepada client diikuti dengan kode status (**HTTP Status Code**).

## HTTP Methods

## HTTP Status Code

## Routes/Endpoints









# Contoh Web Service







































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
https://en.wikipedia.org/wiki/Remote_procedure_call
https://en.wikipedia.org/wiki/XML-RPC
https://www.dicoding.com/blog/apa-itu-web-service/
https://www.guru99.com/web-service-architecture.html
https://www.javatpoint.com/what-is-web-service
https://en.wikipedia.org/wiki/Web_service
https://www.cleo.com/blog/knowledge-base-web-services
https://www.mysqltutorial.org/mysql-sample-database.aspx
