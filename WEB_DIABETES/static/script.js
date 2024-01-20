// Lấy các phần tử DOM cần sử dụng
var Page1 = document.querySelector('.page_1');
var pageQuestion = document.querySelector('.page_question');
var pageNum = document.querySelector('.num-page');
const btnStartNow = document.querySelector('.page1_left-btn');
const btnNext = document.querySelector('.btn-next');
const btnPrev = document.querySelector('.btn-prev');
const btnSub = document.querySelector('#smbt');
var questions = document.querySelectorAll('.question');
var imgQuestion = document.getElementById('img-page_question');
var pageResult = document.querySelector('.page_result');
var btnHome = document.querySelector('.page_result-btnhome');
var currentQuestionIndex = 0;

var listIMG = ['../static/img_1.png','../static/img_2.png','../static/img_3.png','../static/img_4.png','../static/img_5.png','../static/img_6.png','../static/img_7.png','../static/img_8.png','../static/img_9.png','../static/img_10.png','../static/img_11.png','../static/img_12.png','../static/img_13.png','../static/img_14.png','../static/img_15.png','../static/img_result.png'];

// Bắt sự kiện click cho nút bắt đầu
btnStartNow.addEventListener('click', function(){
  Page1.style.display = 'none';
  pageQuestion.style.display = 'flex';
  pageNum.style.display = 'flex';
  // Cập nhật hình ảnh khi bắt đầu
  imgQuestion.src = listIMG[currentQuestionIndex];
});

// Bắt sự kiện click cho nút tiếp theo
btnNext.addEventListener('click', function(){
  console.log(currentQuestionIndex);
  // Ẩn câu hỏi hiện tại và hiển thị câu hỏi tiếp theo
  if (currentQuestionIndex < questions.length - 1) {
    questions[currentQuestionIndex].style.display = "none";
    currentQuestionIndex++;
    questions[currentQuestionIndex].style.display = "flex";
    // Cập nhật hình ảnh
    imgQuestion.src = listIMG[currentQuestionIndex];
  }
  else if(currentQuestionIndex === questions.length - 1) { 
    btnSub.style.display = 'block';
    btnNext.style.display = 'none';
  }
});

// Bắt sự kiện click cho nút trước đó
btnPrev.addEventListener('click', function(){
  // Ẩn câu hỏi hiện tại và hiển thị câu hỏi trước đó
  if (currentQuestionIndex > 0) {
    questions[currentQuestionIndex].style.display = "none";
    currentQuestionIndex--;
    questions[currentQuestionIndex].style.display = "flex";
    // Cập nhật hình ảnh
    imgQuestion.src = listIMG[currentQuestionIndex];
  } else {
    // Nếu là câu hỏi đầu tiên, quay trở lại trang đầu tiên
    pageQuestion.style.display = "none";
    Page1.style.display = 'flex';
    pageNum.style.display = 'none';
  }
});

btnHome.addEventListener('click', function(e){
  location.reload();
});