 - Use `container: $image_name` to run all `steps` in it.
   
   Still needs `runs-on`, but much better than ubuntu-latest as the container image
   is more consistent and portable.
 - How to list caches: 

   ```bash
   gh api -H "Accept: application/vnd.github+json" \
        /repos/${GH_REPO}/actions/caches
   ```
 - How to remove caches:
   
   ```bash
   gh api --method DELETE /repos/${GH_REPO}/actions/caches/$ID
   ```
