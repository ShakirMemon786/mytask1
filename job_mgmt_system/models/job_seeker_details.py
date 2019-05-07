# -*- coding: utf-8 -*-
from flectra import api, fields, models


class JobSeekerDetails(models.Model):
    _name = "job.seeker.details"



    name = fields.Char(string="Name of Applicant")
    degree = fields.Selection([('be', 'BE'),('bca', 'BCA')], string="Degree",)
    user_email = fields.Char(type="char", string="User Email", copy=False)
    job_id = fields.Many2one('job.details', "Applied Job")
    salary_proposed = fields.Float(string="Proposed Salary")
    salary_expected = fields.Float(string="Expected Salary")
    availability = fields.Date(string="Availability")
    phone = fields.Char("Phone", size=12, copy=False)
    mobile = fields.Char("Mobile", size=12)
    _sql_constraints = [
        ('name_uniq', 'unique (mobile)', 'The mobile number of the job seeker must be unique!'), ('name_uniq', 'unique (user_email)', 'The email of the job Seeker for Recruitment must be unique!')
    ]
#    type_id = fields.Many2one('hr.recruitment.degree', "Degree")
#    company_id = fields.Many2one('company.details', "Companys")
    company_details_ids = fields.Many2many("company.details","company_seeker_rel","job_seeker_details_id", "company_details_id", string="Company Details")

    state = fields.Selection([('applied', 'Applied'),('recruted', 'Recruted'),('cancle', 'Application Cancle')], readonly=True)


    @api.multi
    def button_applied(self):
            self.state = "applied"

    @api.multi
    def button_recruted(self):
        self.state = "recruted"

    @api.multi
    def button_cancle(self):
        self.state = "cancle"
