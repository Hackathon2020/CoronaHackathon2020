
/**
 * Removed all child-elements of a given DOM-node
 */
function removeAllChildren(node) {
  while (node.firstChild) {
      node.removeChild(node.lastChild);
  }
}

/**
 * Generates and displays QR-Code encoding the json encoded answers
 *
 * Draws in container with id "qrcode", needs included "js/qrcode.js".
 */
function generate_qr_code_of_answer(answer) {
    var binary_encoded_answer = btoa(JSON.stringify(answer));
    var url = window.location.origin + "/answer?global_id=" + answer.global_questionaire_id + "&data=" + binary_encoded_answer;
    node = document.getElementById("qrcode")
    removeAllChildren(node)
    new QRCode(node, {
        text: url,
        width: 700,
        height: 700,
        colorDark : "#000000",
        colorLight : "#ffffff",
        correctLevel : QRCode.CorrectLevel.L
    });
    console.log("Generated qr-code with url " + url);
}

/**
 * Reads selected radio button
 *
 * Needs html sting input element has class="form-control"
 */
function read_string_answer(question_id) {
    var question_element = document.getElementById("question_" + question_id);
    var answer_element = question_element.getElementsByClassName("form-control")[0];
    return answer_element.value;
}

/**
 * Reads selected radio button
 *
 * Needs radio buttons have class="checkbox" and id="answer_XX"
 */
function read_checkbox_answer(question_id) {
    return read_options(question_id, "checkbox");
}

/**
 * Reads selected radio button
 *
 * Needs radio buttons have class="radio" and id="answer_XX"
 */
function read_radio_answer(question_id) {
    var selections = read_options(question_id, "radio");
    if (selections.length == 1) {
        return selections[0];
    } else {
        console.warn("No or more than one radio button selected: " + selections);
    }
}

/**
 * Helper function
 */
function read_options(question_id, class_name) {
    var question_element = document.getElementById("question_" + question_id);
    var answer_elements = question_element.getElementsByClassName(class_name);
    var answers = [];
    for (i = 0; i < answer_elements.length; i++) {
        if (answer_elements[i].checked) {
            answers.push(answer_elements[i].id.split("_")[1]);
        }
    }
    return answers;
}

/**
 * Collects answers from form data and returns a json answer object
 *
 * Needs surrounding element with class "question" and id "question_" + id
 */
function form_to_answer(questionaire) {
    var answer_map = [];
    var questions = document.getElementsByClassName("question");
    for (i = 0; i < questions.length; i++) {
        var question_id = questions[i].id.split("_")[1];
        // TODO needs questionaire
        var question = find_question(questionaire.question_map, question_id);
        var answer = "";
        switch (question.answer_type) {
            case "String":
                answer = read_string_answer(question_id);
                break;
            case "Checkbox":
                answer = read_checkbox_answer(question_id);
                break;
            case "RadioButtons":
                answer = read_checkbox_answer(question_id);
                break;
            default:
                console.warn("Parsing answers: answer type " + answer_type + " not known!");
        }
        answer_map.push({ "question_id" : question_id , "answer" : answer});
    }
    var answers = { "global_questionaire_id" : questionaire.global_questionaire_id, "answer_map" : answer_map};
    console.log("Answer is: " + JSON.stringify(answers));
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
    var answer = atob(c);
    console.log("Received answer is: " + JSON.stringify(answer));
    return answer;
}

/**
 * Writes answer text to corresponding question html elements
 *
 * Answer element needs class "answer" and surrounding element with id is "answer_" + question id.
 */
function write_answers(answers, questionaire) {
    var list = answers.answer_map;
    for (i = 0; i < list.length; ++i) {
        var question = document.getElementById("answer_" + list[i].question_id);
        var ans_elem = question.getElementsByClassName("answer")[0];
        // FIXME use selected language
        var text = localized_answer(list[i], questionaire, "german");
        var text_elem = document.createTextNode(text.answer_text);
        ans_elem.appendChild(text_elem);
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
function localized_answer(answer, questionaire, language) {
   var question_text = questionaire.language_map[language][answer.question_id]
   var question = find_question(questionaire.question_map, answer.question_id)
   var answer_needs_translation = !(typeof question.options === 'undefined')
   var answer_text = answer.answer
   if (answer_needs_translation) {
     answer_text = questionaire.language_map[language][answer_text]
   }

   return {
     question_text: question_text,
     answer_text: answer_text
   }
}

/**
 * Writes cookie with expiration date
 *
 * From https://www.w3schools.com/js/js_cookies.asp
 */
function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

/**
 * Read cookie with given name
 *
 * Will return empty string if cookie is not available
 *
 * From https://www.w3schools.com/js/js_cookies.asp
 */
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

