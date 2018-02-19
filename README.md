# The ReadThat API
The API provides the following endpoints:


### Get a Single Submission
```
GET /submissions/1/
```

#### Response
```
200 OK

{
  'url': 'https://api.redthat.com/submissions/1/'
  'title': 'List of HTTP Status Codes'
  'external_link': 'https://en.wikipedia.org/wiki/List_of_HTTP_status_codes',
  'upvotes': 0,
  'downvotes': 0
}
```
---


### List All Submissions
```
GET /submissions/
```

A paginated list of all submissions in the database

#### Response
```
200 OK

{
  'count': 1,
  'next': null, # the URL for the next page of results
  'previous': null, # the URL for the previous page of results
  'results': [
    {
      'url': 'https://api.redthat.com/sumbmissions/1/',
      'title': 'List of HTTP Status Code',
      'external_link': 'https://en.wikipedia.org/wiki/List_of_HTTP_status_codes',
      'upvotes': 0,
      'downvotes': 0
    },
    ...
  ]
}
```
---


### Create a New Submission
```
POST /submissions/

{
  'external_link': 'http://www.django-rest-framework.org/api-guide/serializers'
}
```

#### Response
```
201 Created

{
  'url': 'https://api.redthat.com/submissions/2/',
  'title': 'Serializers - Django REST Framework',
  'external_link': 'http://www.django-rest-framework.org/api-guide/serializers',
  'upvotes': 0,
  'downvotes': 0
}
```
---


### Edit an Existing Submission
```
PATCH /submissions/1/

{
  'title': 'List of HTTP Status Codes from Wikipedia'
}
```

#### Response
```
200 OK

{
  'url': 'https://api.redthat.com/submissions/1/',
  'title': 'List of HTTP Status Codes from Wikipedia', # updated
  'external_link': 'https://en.wikipedia.org/wiki/List_of_HTTP_status_codes',
  'upvotes': 0,
  'downvotes': 0
}
```
---


### Upvote an Existing Submission
```
POST /submission/1/upvote/
```

#### Response
```
201 Created

{
  'url': 'https://api.redthat.com/submissions/1/',
  'title': 'List of HTTP Status Codes from Wikipedia', # updated
  'external_link': 'https://en.wikipedia.org/wiki/List_of_HTTP_status_codes',
  'upvotes': 1, # incremented
  'downvotes': 0
}
```
---


### Downvote an Existing Submission
```
POST /submission/1/downvote/
```

#### Response
```
201 Created

{
  'url': 'https://api.redthat.com/submissions/1/',
  'title': 'List of HTTP Status Codes from Wikipedia', # updated
  'external_link': 'https://en.wikipedia.org/wiki/List_of_HTTP_status_codes',
  'upvotes': 0,
  'downvotes': 1 # incremented
}
```
