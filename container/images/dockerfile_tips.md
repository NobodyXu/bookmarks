 1. [Does putting ARG at top of Dockerfile prevent layer re-use?](https://stackoverflow.com/questions/41593135/does-putting-arg-at-top-of-dockerfile-prevent-layer-re-use)
 
 > If you change the value of a build argument all of the layers after that ARG line will be invalidated.
 > So I guess you should include it just before you use the ARG.
