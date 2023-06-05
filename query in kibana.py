#query1
GET book2_index/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "exists": {
            "field": "parent"
          }
        },
        {
          "bool": {
            "must_not": [
              {
                "term": {
                  "parent": ""
                }
              }
            ]
          }
        }
      ]
    }
  }
}


#or this query for 1 question
GET book2_index/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "exists": {
            "field": "parent"
          }
        },
        {
          "regexp": {
            "parent": ".+"
          }
        }
      ]
    }
  }
}
GET book2_index/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "exists": {
            "field": "parent"
          }
        },
        {
          "regexp": {
            "parent": ".+"
          }
        }
      ]
    }
  },
  "size": 0,
  "aggs": {
    "avg_pages_children_books": {
      "avg": {
        "script": {
          "source": "def value = doc['pages.keyword'].value; if (value instanceof Number) { value } else { Double.parseDouble(value) }"
        }
      }
    }
  }
}




#query2




PUT book2_index/_mapping
{
  "properties": {
    "date": {
      "type": "text",
      "fielddata": true
    }
  }
}

GET book2_index/_search
{
  "size": 0,
  "aggs": {
    "public_years": {
      "terms": {
        "field": "date",
        "size": 5,
        "order": {
          "_count": "desc"
        }
      }
    }
  }
}





#query3
PUT book2_index/_mapping
{
  "properties": {
    "format": {
      "type": "text",
      "fielddata": true
    }
  }
}

GET book2_index/_search
{
  "size": 0,
  "aggs": {
    "format_of_each_book": {
      "terms": {
        "field": "format",
        "order": {
          "_count": "desc"
        }
      }
    }
  }
}

GET book2_index/_search
{
  "size": 0,
  "aggs": {
    "format_count": {
      "terms": {
        "field": "format",
        "size": 5
      }
    }
  }
}

