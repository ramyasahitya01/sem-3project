function popup(id0, id1, id2, download_img_id, download_img_url,user_id,like_act,li,user, likes) {

   var modal = document.getElementById(id0);

   // Get the image and insert it inside the modal - use its "alt" text as a caption
   var img = document.getElementById(id1);
   var modalImg = document.getElementById(id2);
   var dwnld_img = document.getElementById(download_img_id);
   var userid=document.getElementById(user_id);
   var li = document.getElementById(li);
   dwnld_img.setAttribute("href", download_img_url);
   li.setAttribute("action",like_act);
 img.onclick = function () {
       modal.style.display = "block";
       modalImg.src = this.src;
       userid.innerHTML = this.alt;
   };
 document.getElementById(user_id).setAttribute('href', user);


   window.onclick = function(event) {
       if (event.target == modal) {
           modal.style.display = "none";
           }
   };

   var span = document.getElementsByClassName("close")[0];
   // When the user clicks on <span> (x), close the modal
   span.onclick = function () {
       modal.style.display = "none";
   };
   document.getElementById('likes').innerHTML = likes;
}
