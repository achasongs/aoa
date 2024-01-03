function showSidebar(){    //call the onclick function in the menu button so the menu can show
    const sidebar = document.querySelector('.sidebar'); //declare a variable and get the class Sidebar
    sidebar.style.display = 'flex';                 
 }
 function hideSidebar(){    //call the onclick function in the close button so the menu can  close
    const sidebar = document.querySelector('.sidebar'); //declare a variable and get the class Sidebar
    sidebar.style.display = 'none';
 }

 document.addEventListener("DOMContentLoaded", function () {
    var navbar = document.getElementById("nav");
    var linkcolor = document.querySelectorAll(".link-color");

    window.addEventListener("scroll", function () {
        if (window.scrollY > 0) {
            navbar.style.backgroundColor = "#fff"; // Change to your desired background color
            navbar.style.boxShadow = "0 4px 6px rgba(0, 0, 0, 0.1)"; // Change to your desired box shadow
            for(var i = 0; i<linkcolor.length; i++){
                linkcolor[i].style.color = "#333";
            }
        } else {
            navbar.style.backgroundColor = "transparent";
            navbar.style.boxShadow = "none";
            for(var i = 0; i<linkcolor.length; i++){
                linkcolor[i].style.color = "#fff";
            }                                                                           
        }
    });
});


