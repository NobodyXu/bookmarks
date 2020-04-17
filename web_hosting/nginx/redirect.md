### http to https

[301 redirect will be cached **forever**], so use [302 redirect] instead unless you need [SEO].

Otherwise, you may:

 > This indefinite caching is only the default caching by these browsers in the absence of Cache-Control headers. The logic is that you are specifying a "permanent" redirect and not giving them any other caching instructions, so they'll treat it as if you wanted it indefinitely cached.
 > 
 > The browsers still honor the Cache-Control and Expires headers like with any other response, if they are specified.
 > 
 > You can add headers such as Cache-Control: max-age=3600 or Expires: Thu, 01 Dec 2014 16:00:00 GMT to your 301 redirects. You could even add Cache-Control: no-cache so it won't be cached permanently by the browser or Cache-Control: no-store so it can't even be stored in temporary storage by the browser.



[301 redirect will be cached **forever**]: https://stackoverflow.com/questions/9130422/how-long-do-browsers-cache-http-301s
[302 redirect]: https://stackoverflow.com/questions/12212839/how-long-is-a-302-redirect-saved-in-browser
[SEO]: https://en.wikipedia.org/wiki/Search_engine_optimization
