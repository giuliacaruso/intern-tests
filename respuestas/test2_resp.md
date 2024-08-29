1. The function is checking a list of web pages, and for each of them is returning their information.
If the request to the page is successful (status_code==200), the element 'div' with class 'example-class' is searched and its contained text is returned.
If the request is unsuccessful (status_code=404), a message is printed and None is returned.
If there is a network problem, it raise an exception, it prints an error message and None is returned.

2. Sequential web scraping is useful when dealing with few web pages and when access order is important.
Concurrent web scraping is useful when there is a large amount of web pages, to use a parallel process to reduce the total scraping time, but it cannot take into account the access order.