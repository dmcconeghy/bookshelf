import requests

'''
    Google Books API URIS:
    
    https://www.googleapis.com/books/v1/{collectionName}/resourceID?parameters

    Requests sent to:
    https://www.googleapis.com/books/v1/volumes?q=isbn:{{book.isbn}}&callback=handleResponse

    return a item object from which we can extract the 
    title, author, description, image_url, isbn, and year.

    title: item.volumeInfo.title
    author: item.volumeInfo.authors[0]
    description: item.volumeInfo.description
    image_url: item.volumeInfo.imageLinks.thumbnail
    isbn: item.volumeInfo.industryIdentifiers[0].identifier

    official Resource Representations:

    {
    "kind": "books#volume",
    "id": string,
    "etag": string,
    "selfLink": string,
    "volumeInfo": {
        "title": string,
        "subtitle": string,
        "authors": [
        string
        ],
        "publisher": string,
        "publishedDate": string,
        "description": string,
        "industryIdentifiers": [
        {
            "type": string,
            "identifier": string
        }
        ],
        "pageCount": integer,
        "dimensions": {
        "height": string,
        "width": string,
        "thickness": string
        },
        "printType": string,
        "mainCategory": string,
        "categories": [
        string
        ],
        "averageRating": double,
        "ratingsCount": integer,
        "contentVersion": string,
        "imageLinks": {
        "smallThumbnail": string,
        "thumbnail": string,
        "small": string,
        "medium": string,
        "large": string,
        "extraLarge": string
        },
        "language": string,
        "previewLink": string,
        "infoLink": string,
        "canonicalVolumeLink": string
    },
    "userInfo": {
        "review": mylibrary.reviews Resource,
        "readingPosition": mylibrary.readingpositions Resource,
        "isPurchased": boolean,
        "isPreordered": boolean,
        "updated": datetime
    },
    "saleInfo": {
        "country": string,
        "saleability": string,
        "onSaleDate": datetime,
        "isEbook": boolean,
        "listPrice": {
        "amount": double,
        "currencyCode": string
        },
        "retailPrice": {
        "amount": double,
        "currencyCode": string
        },
        "buyLink": string
    },
    "accessInfo": {
        "country": string,
        "viewability": string,
        "embeddable": boolean,
        "publicDomain": boolean,
        "textToSpeechPermission": string,
        "epub": {
        "isAvailable": boolean,
        "downloadLink": string,
        "acsTokenLink": string
        },
        "pdf": {
        "isAvailable": boolean,
        "downloadLink": string,
        "acsTokenLink": string
        },
        "webReaderLink": string,
        "accessViewStatus": string,
        "downloadAccess": {
        "kind": "books#downloadAccessRestriction",
        "volumeId": string,
        "restricted": boolean,
        "deviceAllowed": boolean,
        "justAcquired": boolean,
        "maxDownloadDevices": integer,
        "downloadsAcquired": integer,
        "nonce": string,
        "source": string,
        "reasonCode": string,
        "message": string,
        "signature": string
        }
    },
    "searchInfo": {
        "textSnippet": string
    }
    }

'''

def get_book_details(isbn):
    """
    
        Get book details from Google Books API.

        From the API we get the following data:
        - title
        - author (first author) TODO: handle multiple authors 
        - description 
        - image_url TODO: handle no image or multiple images
        - published_date
    
        TODO: add publisher for citations.

        Returns None if no book is found.
    
    """

    print(f'getting book details for {isbn}')

    api_response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}')

    if api_response.status_code == 200:
        api_json_response = api_response.json()

        json_data = {
            'book_title': api_json_response['items'][0]['volumeInfo']['title'] or None,
            'book_first_author': api_json_response['items'][0]['volumeInfo']['authors'][0] or None,
            # 'book_publisher': api_json_response['items'][0]['volumeInfo']['publisher'] or None,
            'book_description': api_json_response['items'][0]['volumeInfo']['description'] or None,
            'book_image_url': api_json_response['items'][0]['volumeInfo']['imageLinks']['thumbnail'] or None,
            'book_published_date': (api_json_response['items'][0]['volumeInfo']['publishedDate'])[0:4]
        }

        return json_data

    else: 
        api_response.status_code == 404

        print(f'404 error: {api_response.json()}')

        return None 