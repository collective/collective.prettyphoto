jq(document).ready(function(){
    jq(document).ready(function(){
        // add rel tag for all links with class 'prettyPhoto'

        jq("a.prettyPhoto").attr({"rel": "prettyPhoto"});

        jq("a.prettyPhoto img").each(function(index,value) {
          var imgurl = jq(value).attr("src");
          var lastunderscore = imgurl.lastIndexOf("_");
          var imagebase = imgurl.slice(0,lastunderscore);
          jq(value).parent("a.prettyPhoto").attr("href",imagebase + "_large");
        });
        // add iframe attributes for all links with class 'prettyPhotoIframe'
        jq("a.prettyPhotoIframe").attr("href", function() {
            return this.href + "?iframe=true&width=75%&height=75%";
        }).attr({"rel": "prettyPhoto"});

        // enable prettyPhoto
        jq("a[rel^='prettyPhoto']").prettyPhoto({theme:'light_rounded'});
    });
});
