
      // .search
      window.addEventListener("DOMContentLoaded", () => {
        // body.querySer.addEventListener('click')
        var search = document.querySelector(".search");
        var searchBtn = document.querySelector(".form-btn");
        var clicked = searchBtn.previousElementSibling;
        searchBtn.addEventListener("click", function (e) {
          e.preventDefault();

          document.body.classList.toggle("active-search");
        });
        document.body.addEventListener("click", function (e) {
          // if (e.target != search && clicked.classList.contains("active")) {
          //   // alert("123");
          //   // if (e.target != search) {
          //   clicked.classList.remove("active");
          //   document.body.classList.remove("active-search");
          //   // }
          // }
          // document.body.classList.toggle("active-burger");

          if (
            !e.target.closest(".search") &&
            document.body.closest(".active-search")
          ) {
            document.body.classList.remove("active-search");
          }

          // if (clicked.classList.contains("active-search")) {
          // if (e.target != clicked) {
          //   console.log(e.target);
          // } else {
          //   console.log(12345);
          // }
          // clicked.classList.toggle("active-search");
          // document.body.classList.toggle("active-search");
          // }
        });
      });


      window.addEventListener("DOMContentLoaded", () => {
        let swiper = new Swiper(".mySwiper", {
          direction: "vertical",
          autoplay: {
            delay: 3500,
          },
          // loop: true,
          slidesPerView: 4,
          spaceBetween: 30,
          on: {
            slideChange: function (swiper) {
              var activeSlide = swiper.activeIndex;
              var activeTabs = document.querySelectorAll(
                ".tab-pane.active.show"
              );
              activeTabs.forEach((elem) => {
                elem.classList.remove("show");
                elem.classList.remove("active");
              });
              swiper.slides[activeSlide].click();
            },
            slideChangeTransitionStart: function (swiper) {},
          },
        });
      });





      // .search
      window.addEventListener("DOMContentLoaded", () => {
        // body.querySer.addEventListener('click')
        var search = document.querySelector(".search");
        var searchBtn = document.querySelector(".form-btn");
        var clicked = searchBtn.previousElementSibling;
        searchBtn.addEventListener("click", function (e) {
          e.preventDefault();

          document.body.classList.toggle("active-search");
        });
        document.body.addEventListener("click", function (e) {
          if (
            !e.target.closest(".search") &&
            document.body.closest(".active-search")
          ) {
            document.body.classList.remove("active-search");
          }
        });
        const lightbox = GLightbox({
          touchNavigation: true,
          loop: true,
          autoplayVideos: true,
        });
      });


