import urllib.request as urllib
         
def main(url):
   print("checking connectivity")

   response = urllib.urlopen(url)
   print("connected to", url, "successfully")
   print("the response code was:", response.getcode())


print("a site connectivity checker program")
input_url = input ("please input the url")

main(input_url)


    

