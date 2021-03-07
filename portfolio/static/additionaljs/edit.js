//Static variables
addRowQual.count = 0;
addRowSkill.count = 0;
addRowSocial.count = 0;
addRowWork.count = 0;


//Qualification Functions
//Add row for Qualifications
function addRowQual() {
  addRowQual.count++;
  if (addRowQual.count != 1) {
    var rem = document.getElementById('rmvbtnqual');
    rem.parentNode.removeChild(rem);
  }
  var rowhtml = `<div class="container" name="rowqual` + addRowQual.count + `" id="rowqual` + addRowQual.count + `">
                    <div class="row g-2">
                      <div class="col-6 form-floating mb-3">
                        <input type="text" name="degreename`+ addRowQual.count + `" class="form-control" id="input1" placeholder="Degree Name" required>
                        <label style="color: #000;" for="input1">Degree Name</label>
                        <div class="invalid-feedback">
                          Please fill out this field
                        </div>
                      </div>
                      <div class="col-6 form-floating mb-3">
                        <input type="text" name="degreedate`+ addRowQual.count + `" class="form-control" id="input2" placeholder="Degree Date" required>
                        <label style="color: #000;" for="input2">Degree Date</label>
                        <div class="invalid-feedback">
                          Please fill out this field
                        </div>
                      </div>
                    </div>
                    <div class="row g-2">
                      <div class="col-6 form-floating mb-3">
                        <input type="text" name="degreefrom`+ addRowQual.count + `" class="form-control" id="input3" placeholder="University" required>
                        <label style="color: #000;" for="input3">University</label>
                        <div class="invalid-feedback">
                          Please fill out this field
                        </div>
                      </div>
                      <div class="col-6 form-floating mb-3">
                        <input type="text" name="degreegpa`+ addRowQual.count + `" class="form-control" id="input4" placeholder="GPA">
                        <label style="color: #000;" for="input4">GPA</label>
                      </div>
                    </div>
                    <input type="button" class="btn btn-danger btn-sm col-2 float-md-end" id="rmvbtnqual" value="Delete" onclick="removeRowQual(this)">
                  </div>`;
  document.querySelector('#qualcontent').insertAdjacentHTML(
    'beforeend',
    rowhtml
  )
}

//Remove row for qualifications
function removeRowQual(input) {
  input.parentNode.remove();
  addRowQual.count--;
  if (addRowQual.count != 0) {
    var currentrow = '#rowqual' + addRowQual.count;
    document.querySelector(currentrow).insertAdjacentHTML(
      'beforeend',
      '<input type="button" class="btn btn-danger btn-sm col-2 float-md-end" id="rmvbtnqual" value="Delete" onclick="removeRowQual(this)">'
    )
  }
}

//Skill Functions
//Add row for Skills
function addRowSkill() {
  addRowSkill.count++;
  if (addRowSkill.count != 1) {
    var rem = document.getElementById('rmvbtnskill');
    rem.parentNode.removeChild(rem);
  }
  var rowhtml = `<div class="col-8" id = "rowskill` + addRowSkill.count + `">
                   <div class="form-floating mb-3">
                     <input type="text" name="skillname`+ addRowSkill.count + `"class="form-control" id="input1" placeholder="Add Skill" required>
                     <label style="color: #000;" for="input1">Add Skill</label>
                    <div class="invalid-feedback">
                      Please fill out this field
                    </div>
                  </div>
                    <input type="button" class="btn btn-danger btn-sm col-2 float-md-end" id="rmvbtnskill" value="Delete" onclick="removeRowSkill(this)">
                   </div>`;
  document.querySelector('#skillcontent').insertAdjacentHTML(
    'beforeend',
    rowhtml
  )
}

//Remove row for Skills
function removeRowSkill(input) {
  input.parentNode.remove();
  addRowSkill.count--;
  if (addRowSkill.count != 0) {
    var currentrow = '#rowskill' + addRowSkill.count;
    document.querySelector(currentrow).insertAdjacentHTML(
      'beforeend',
      '<input type="button" class="btn btn-danger btn-sm col-2 float-md-end" id="rmvbtnskill" value="Delete" onclick="removeRowSkill(this)">'
    )
  }
}

//Social Functions
//Add row for Social
function addRowSocial() {
  addRowSocial.count++;
  if (addRowSocial.count != 1) {
    var rem = document.getElementById('rmvbtnsocial');
    rem.parentNode.removeChild(rem);
  }
  var rowhtml = `<div class="container" id = "rowsocial` + addRowSocial.count + `">
                  <div class="row g-2">
                    <div class="col-md">
                      <div class="">
                        <input class="form-control" list="socialOptions" id="socialDataList" placeholder="Social Media" required>
                        <datalist id="socialOptions">
                          <option value="Facebook">
                          <option value="Twitter">
                          <option value="Instagram">
                          <option value="GitHub">
                        </datalist>
                        <div class="invalid-feedback">
                          Please fill out this field
                        </div>
                      </div>
                    </div>
                    <div class="col-md">
                      <div class="input-group mb-3">
                        <span class="input-group-text" id="basic-addon1">@</span>
                        <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1" required>
                        <div class="invalid-feedback">
                          Please fill out this field
                        </div>
                      </div>
                    </div>
                  </div>
                  <input type="button" class="btn btn-danger btn-sm col-2 float-md-end" id="rmvbtnsocial" value="Delete" onclick="removeRowSocial(this)">
                </div>`;
  document.querySelector('#socialcontent').insertAdjacentHTML('beforeend', rowhtml);
}

//Remove row for Skills
function removeRowSocial(input) {
  input.parentNode.remove();
  addRowSocial.count--;
  if (addRowSocial.count != 0) {
    var currentrow = '#rowsocial' + addRowSocial.count;
    document.querySelector(currentrow).insertAdjacentHTML(
      'beforeend',
      '<input type="button" class="btn btn-danger btn-sm col-2 float-md-end" id="rmvbtnsocial" value="Delete" onclick="removeRowSocial(this)">'
    )
  }
}

//Work Functions
//Add row for Work
function addRowWork() {
  addRowWork.count++;
  if (addRowWork.count != 1) {
    var rem = document.getElementById('rmvbtnwork');
    rem.parentNode.removeChild(rem);
  }
  var rowhtml = `<div class="container" id="rowwork` + addRowWork.count + `">
                  <div class="row g-2">
                    <div class="form-floating mb-3 col-6">
                      <input type="text" name="jobtitle`+ addRowWork.count + `" class="form-control" id="input1" placeholder="Job Title" required>
                      <label style="color: #000;" for="input1">Job Title</label>
                      <div class="invalid-feedback">
                        Please fill out this field
                      </div>
                    </div>
                    <div class="form-floating mb-3 col-6">
                      <input type="text" name="companyname`+ addRowWork.count + `" class="form-control" id="input2" placeholder="Company Name" required>
                      <label style="color: #000;" for="input2">Company Name</label>
                      <div class="invalid-feedback">
                        Please fill out this field
                      </div>
                    </div>
                  </div>
                  <div class="row g-2">
                    <div class="form-floating mb-3 col-6">
                      <input name="startdate`+ addRowWork.count + `" type="date" id="start-date" class="form-control" required>
                      <label for="start-date" style="color: black;">Start Date</label>
                      <div class="invalid-feedback">
                        Please fill out this field
                      </div>
                    </div>
                    <div class="form-floating mb-3 col-6">
                      <input name="enddate`+ addRowWork.count + `" type="date" id="end-date" class="form-control" required>
                      <label for="end-date" style="color: black;">End Date</label>
                      <div class="invalid-feedback">
                        Please fill out this field
                      </div>
                    </div>
                  </div>
                  <input type="button" class="btn btn-danger btn-sm col-2 float-md-end" id="rmvbtnwork" value="Delete" onclick="removeRowWork(this)">
                 </div>`;
  document.querySelector('#workcontent').insertAdjacentHTML('beforeend', rowhtml);
}

//Remove row for Work
function removeRowWork(input) {
  input.parentNode.remove();
  addRowWork.count--;
  if (addRowWork.count != 0) {
    var currentrow = '#rowwork' + addRowWork.count;
    document.querySelector(currentrow).insertAdjacentHTML(
      'beforeend',
      '<input type="button" class="btn btn-danger btn-sm col-2 float-md-end" id="rmvbtnwork" value="Delete" onclick="removeRowWork(this)">'
    )
  }
}