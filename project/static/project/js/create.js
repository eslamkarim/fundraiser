var img = document.getElementById("img")
img.addEventListener("change",function(e){
  document.getElementById("noFile").textContent=e.target.files[0].name
 
})

var img = document.getElementById("img2")
img.addEventListener("change",function(e){
  document.getElementById("noFile2").textContent=""
  for (let i=0 ; i< e.target.files.length; ++i){
    document.getElementById("noFile2").textContent+=e.target.files[i].name + " , "

  }
 
})
