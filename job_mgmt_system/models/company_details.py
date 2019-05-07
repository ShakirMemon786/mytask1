# -*- coding: utf-8 -*-
from flectra import api, fields, models


class CompanyDetails(models.Model):
    _name = "company.details"

    name = fields.Char(string="Company Name",)
    location = fields.Text(string="Company Address Location")
    description = fields.Text(string="Description")
    start_date = fields.Date(string="Start date")
    job_id = fields.Many2one("job.details", required=True, string="Jobs")
    job_seeker_ids = fields.Many2many("job.seeker.details", "company_seeker_rel", 'company_details_id',
                                          'job_seeker_details_id', string='job seekers', readonly="True")
