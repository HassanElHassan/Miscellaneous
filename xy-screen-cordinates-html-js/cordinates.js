// view x/y screen coordinates in console on Shift+mouse click on page

document.addEventListener(

    "DOMContentLoaded", 

    function () {
        
        document.querySelector("html").addEventListener("click", 
            function (event) {
                if (event.shiftKey === true) {
                    console.log("x: " + event.clientX)
                    console.log("y: " + event.clientY)
                }
            }
        )
    }
    
);
