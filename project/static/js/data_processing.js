/**
 * Generates and displays QR-Code encoding the json encoded answers
 *
 * Draws in container with id "qrcode", needs included "js/qrcode.js".
 */
function generate_qr_code_of_answer(answer) {
    var binary_encoded_answer = btoa(JSON.stringify(variable1));
    var url = window.location.origin + "/answer?global_id=" + answer.global_questionaire_id + "&data=" + binary_encoded_answer;
    // FIXME calculate width and height according to window
    new QRCode(document.getElementById("qrcode"), {
        text: url,
        width: 700,
        height: 700,
        colorDark : "#000000",
        colorLight : "#ffffff",
        correctLevel : QRCode.CorrectLevel.L
    });
}

/**
 * Collects answers from form data and returns a json answer object
 *
 * Needs surrounding element with class "question" and id "question_" + id
 * TODO needs implementation
 */
function form_to_answer() {
    var answer_map;
    var questions = document.getElementsByClassName("question");
    for (i = 0; i < questions.length; i++) {
        var question_id = questions[i].id.split("_")[1];
        // TODO needs questionaire
        var question = find_question(questionaire, question_id);
        // TODO get data from answer fields depending on answer type
        answer_map.push({ "question_id" : question_id , "answer" : "TODO" });
    }
    var answers = { "global_questionaire_id" : "TODO", "answer_map" : answer_map};
    return answers;
}

/**
 * Gets answer encoded in url of current location
 *
 * returns json object of answer
 */
function get_answer_from_url() {
    var url = window.location.href;
    var c = url.searchParams.get("data");
    return atob(c);
}

/**
 * Writes answer text to corresponding question html elements
 *
 * Answer element needs class "answer" and surrounding element with id is "question_" + question id.
 */
function write_answers(answers) {
    var list = answers.answer_map;
    for (i = 0; i < list.length; ++i) {
        var question = document.getElementById("question_" + list[i].question_id);
        var ans_elem = question.getElementsByClassName("answer");
        // TODO needs questionaire
        // FIXME use selected language
        var text = localized_answer(list[i], questionaire, "german");
        var text_elem = document.createTextNode(text.answer_text);
        ans_elem.appendChild(text);
    }
}

/**
 * Helper function
 */
function find_question(question_map, question_id) {
  for (i = 0; i < question_map.length; ++i) {
    if (question_map[i].question_id === question_id) {
      return question_map[i]
    }
  }
}

/**
 * Helper function
 */
function localized_anwser(anwser, questionaire, language) {
   var question_text = questionaire.language_map[language][anwser.question_id]
   var question = find_question(questionaire.question_map, anwser.question_id)
   var anwser_needs_translation = !(typeof question.options === 'undefined')
   var anwser_text = anwser.answer
   if (anwser_needs_translation) {
     anwser_text = questionaire.language_map[language][anwser_text]
   }

   return {
     question_text: question_text,
     anwser_text: anwser_text
   }
}
