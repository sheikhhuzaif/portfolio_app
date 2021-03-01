//Static variables
addRowQual.count=0;
addRowSkill.count=0;
addRowSocial.count=0;

//Qualification Functions
//Add row for Qualifications
function addRowQual () {
  addRowQual.count++;
  if(addRowQual.count!=1){
  var rem = document.getElementById('rmvbtnqual');
  rem.parentNode.removeChild(rem);
  }
  var rowhtml = `<div class="row" id="rowqual`+addRowQual.count+`">
                  <input type="text" name="degreename`+addRowQual.count+`" id="" class="" placeholder="Degree Name">
                  <input type="text" name="degreedate`+addRowQual.count+`" id="" class="" placeholder="Year of Passing">
                  <input type="text" name="degreeform`+addRowQual.count+`" id="" class="" placeholder="Board/University">
                  <input type="text" name="degreegpa`+addRowQual.count+`" id="" class=""  placeholder="Percentage %">
                  <input type="button" id="rmvbtnqual" value="Delete Row" onclick="removeRowQual(this)">
                  </div>`;
  document.querySelector('#qualcontent').insertAdjacentHTML(
    'beforeend',
    rowhtml
  )
}

//Remove row for qualifications
function removeRowQual (input) {
    input.parentNode.remove();
    addRowQual.count--;
    if(addRowQual.count!=0){
    var currentrow = '#rowqual'+addRowQual.count;
    document.querySelector(currentrow).insertAdjacentHTML(
      'beforeend',
      '<input type="button" id="emvbtnqual" value="Delete Row" onclick="removeRowQual(this)">'
    )
    }
  }

//Skill Functions
//Add row for Skills
function addRowSkill () {
    addRowSkill.count++;
    if(addRowSkill.count!=1){
    var rem = document.getElementById('rmvbtnskill');
    rem.parentNode.removeChild(rem);
    }
    var rowhtml = `<div class="row" id="rowskill`+addRowSkill.count+`">
                    <input type="text" name="skillname`+addRowSkill.count+`" placeholder="Skill name..." >
                    <input type="button" id="rmvbtnskill" value="Delete Row" onclick="removeRowSkill(this)">
                    </div>`;
    document.querySelector('#skillcontent').insertAdjacentHTML(
      'beforeend',
      rowhtml
    )
}

//Remove row for Skills
function removeRowSkill (input) {
    input.parentNode.remove();
    addRowSkill.count--;
    if(addRowSkill.count!=0){
    var currentrow = '#rowskill'+addRowSkill.count;
    document.querySelector(currentrow).insertAdjacentHTML(
      'beforeend',
      '<input type="button" id="rmvbtnskill" value="Delete Row" onclick="removeRowSkill(this)">'
    )
    }
}

//Social Functions
//Add row for Social
function addRowSocial () {
    addRowSocial.count++;
    if(addRowSocial.count!=1){
    var rem = document.getElementById('rmvbtnsocial');
    rem.parentNode.removeChild(rem);
    }
    var rowhtml = `<div class="row" id="rowsocial`+addRowSocial.count+`">
                    <input type="text" id="username`+addRowSocial.count+`" class="" placeholder="UserName">
                    <input type="text" id="link`+addRowSocial.count+`" class="" placeholder="Link">  
                    <input type="button" id="rmvbtnsocial" value="Delete Row" onclick="removeRowSocial(this)">
                   </div>`;
    document.querySelector('#socialcontent').insertAdjacentHTML(
      'beforeend',
      rowhtml
    )
}

//Remove row for Skills
function removeRowSocial (input) {
    input.parentNode.remove();
    addRowSocial.count--;
    if(addRowSocial.count!=0){
    var currentrow = '#rowsocial'+addRowSocial.count;
    document.querySelector(currentrow).insertAdjacentHTML(
      'beforeend',
      '<input type="button" id="rmvbtnsocial" value="Delete Row" onclick="removeRowSocial(this)">'
    )
    }
}