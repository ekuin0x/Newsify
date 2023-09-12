$("head").prepend(head)
(async()=>{
    const q = $("#q").attr("name")
    url = `/related/${q}`
    const res2 = await fetch(url)
    const related = await res2.text()
   $("#related").html(related)
})

let head = 
"<script async src='https://www.googletagmanager.com/gtag/js?id=G-KBVD10W104'></script><script>"+
"window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}"+
"gtag('js', new Date());gtag('config', 'G-KBVD10W104');</script>"

const search = async ()=>{
    let query = $("#query").val()
    let searchHtml = await fetch('/search/' + query )
    let res = await searchHtml.text()
    $("#wrapper").html(res)
}

