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

                <div class="form-floating mb-3">
                <input type="text" name="degreename`+addRowQual.count+`" class="form-control" id="input1" placeholder="Degree Name">
                <label style="color: #000;" for="input1">Degree Name</label>
                </div>
                <div class="form-floating mb-3">
                <input type="text" name="degreedate`+addRowQual.count+`" class="form-control" id="input2" placeholder="Degree Date">
                <label style="color: #000;" for="input2">Degree Date</label>
                </div>
                <div class="form-floating mb-3">
                <input type="text" name="degreefrom`+addRowQual.count+`" class="form-control" id="input3" placeholder="Year of Passing">
                <label style="color: #000;" for="input3">Year of Passing</label>
                </div>
                <div class="form-floating mb-3">
                <input type="text" name="degreegpa`+addRowQual.count+`" class="form-control" id="input4" placeholder="GPA">
                <label style="color: #000;" for="input4">GPA</label>
                </div>
                  <input type="button" class="btn btn-outline-danger btn-sm" id="rmvbtnqual" value="Delete Row" onclick="removeRowQual(this)">
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
      '<input type="button" class="btn btn-outline-danger btn-sm" id="emvbtnqual" value="Delete Row" onclick="removeRowQual(this)">'
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
                    <input type="button" class="btn btn-outline-danger btn-sm" id="rmvbtnskill" value="Delete Row" onclick="removeRowSkill(this)">
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
      '<input type="button" class="btn btn-outline-danger btn-sm" id="rmvbtnskill" value="Delete Row" onclick="removeRowSkill(this)">'
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
    var rowhtml = `<div class="row g-2" id="rowsocial`+addRowSocial.count+`">
                     <div class="col-md">
                        <div class="">
                          <input class="form-control" list="socialOptions" id="socialDataList" placeholder="Social Media">
                          <datalist id="socialOptions">
                          <option value="Facebook">
                          <option value="Twitter">
                          <option value="Instagram">
                          <option value="GitHub">
                          </datalist>
                        </div>
                      </div>
                     <div class="col-md">
                     <div class="input-group mb-3">
                     <span class="input-group-text" id="basic-addon1">@</span>
                     <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1">
                     </div>
                     </div>
                     <input type="button" class="btn btn-outline-danger btn-sm" id="rmvbtnsocial" value="Delete Row" onclick="removeRowSocial(this)">
                   </div>`;
    document.querySelector('#socialcontent').insertAdjacentHTML('beforeend',rowhtml);
}

//Remove row for Skills
function removeRowSocial (input) {
    input.parentNode.remove();
    addRowSocial.count--;
    if(addRowSocial.count!=0){
    var currentrow = '#rowsocial'+addRowSocial.count;
    document.querySelector(currentrow).insertAdjacentHTML(
      'beforeend',
      '<input type="button" class="btn btn-outline-danger btn-sm" id="rmvbtnsocial" value="Delete Row" onclick="removeRowSocial(this)">'
    )
    }
}