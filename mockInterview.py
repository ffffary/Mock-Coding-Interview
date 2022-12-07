####################################################################################
#-------------------------------Mock Coding:12/6 ----------------------------------#
####################################################################################
# status codes serve as a means of communication between the server and the internet browser
# 1xx: informational 
# 2xx: success(the client’s request was accepted successfully.)
# 3xx: redirection(the client must take some additional action in order to complete their request.)
# 4xx: client error
# 5xx: server error
# 429 Too Many Requests: The user has sent too many requests in a given amount of time (“rate limiting”).

####################################################################################
#-----------------------------Part 1: basic version--------------------------------#
####################################################################################
class Error(Exception):
    # base class for other exceptions
    pass

class BadStatusError(Error):
    # raised when gets an bad status code
    __module__ = Exception.__module__

class TooManyRequestsError(Error):
    # raised when requests over the limit
    __module__ = Exception.__module__ 

def api_call(): 
   return {
      "status": 202, 
       "text": "hello",
    }

def retry():
    result = api_call()
    status_code = result.get("status")

    if status_code == 200:
        print(result)
    else:
        raise BadStatusError("Bad Status")
retry() 

# bad program runs forever
# def retry():
#     hash_table = api_call()
#     status_code = hash_table.get("status")

#     if status_code == 200:
#         print(hash_table)
#         return api_call()
#     else:
#         print("error")
#         return retry()
# retry() 

####################################################################################
#-----------------------------Part 2: while loop used------------------------------#
####################################################################################
class Error(Exception):
    # base class for other exceptions
    pass
class BadStatusError(Error):
    # raised when gets an bad status code
    __module__ = Exception.__module__ 
class TooManyRequestsError(Error):
    # raised when requests over the limit
    __module__ = Exception.__module__ 

def api_call(): 
   return {
      "status": 202, 
       "text": "hello",
    }

def retry():
    result = api_call()
    status_code = result.get("status")

    if status_code == 200:
        print("Hello")
    elif status_code == 429:
        retries = 0
        max_retry = 10
        while retries < max_retry:
            retries += 1
            result
        raise TooManyRequestsError("Too Many Requests!")
    else:
        raise BadStatusError("Bad Status Error!")

####################################################################################
#-----------------------------Part 3: recursion used------------------------------#
####################################################################################
def api_call(): 
   return {
      "status": 429, 
       "text": "hello",
    }

def retry(max_retry):
    result = api_call()
    status_code = result.get("status")
    
    if status_code == 200:
        return result.get("text")
    elif status_code == 429:
        if max_retry > 0:
            return retry(max_retry-1)
        return "Too many requests!"
    else:
        return "bad status!"

####################################################################################
#------------------------Part 4: recursion with test cases-------------------------#
#test plan: try statusCode 429, 200, 300 one by one
#test cases:
#test case 1: set statusCode to be 429, should output "Too many requests!"
#test case 2: set statusCode to be 200, should output "hello"
#test case 3: set statusCode to be 300, should output "bad status!"
####################################################################################

import unittest

def api_call(): 
   return {
      "status": 429, 
       "text": "hello",
    }

def retry(max_retry):
    result = api_call()
    status_code = result.get("status")
    
    if status_code == 200:
        # print("hello")
        # return result
        return result.get("text")
    elif status_code == 429:
        if max_retry > 0:
            return retry(max_retry-1)
            
        # print("Too many requests!")
        return "Too many requests!"
    else:
        # print("error!")
        return "bad status!"


class testProgram(unittest.TestCase):
    def test_case_1(self): #set status to be 429
        max_retry = 10
        expected = "Too many requests!"
        self.assertEqual(retry(max_retry), expected)

    # def test_case_2(self): #set status to be 200
    #     max_retry = 10
    #     expected = "hello"
    #     self.assertEqual(retry(max_retry), expected)

    # def test_case_3(self): #set status to be 300
    #     max_retry = 10
    #     expected = "bad status!"
    #     self.assertEqual(retry(max_retry), expected)

if __name__ == '__main__':
    unittest.main()

####################################################################################
#----------------------Part 5: recursion with error handling-----------------------#
####################################################################################
class Error(Exception):
    # base class for other exceptions
    pass
class BadStatusError(Error):
    # raised when gets an bad status code
    __module__ = Exception.__module__ 
class TooManyRequestsError(Error):
    # raised when requests over the limit
    __module__ = Exception.__module__ 

def api_call(): 
   return {
      "status": 429, 
       "text": "hello",
    }

def retry(max_retry):
    result = api_call()
    status_code = result.get("status")
    
    if status_code == 200:
        print("hello")
        return result
    elif status_code == 429:
        if max_retry > 0:
            # print("Too many requests")
            return retry(max_retry-1)
        else:
            raise TooManyRequestsError('Too many requests!')      
    else:
        # print("error!")
        raise BadStatusError("Bad status!")
retry(10)