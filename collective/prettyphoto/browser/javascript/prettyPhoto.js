jq(document).ready(function(){
    jq(document).ready(function(){
        // add rel tag for all links with class 'prettyPhoto'
        jq("a.prettyPhoto").attr({"rel": "prettyPhoto"});

        // add iframe attributes for all links with class 'prettyPhotoIframe'
        jq("a.prettyPhotoIframe").attr("href", function() { 
            return this.href + "?iframe=true&width=75%&height=75%";
        }).attr({"rel": "prettyPhoto"});

        // enable prettyPhoto
        jq("a[rel^='prettyPhoto']").prettyPhoto({theme:'light_rounded'});
    });
});