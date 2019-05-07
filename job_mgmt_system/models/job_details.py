# -*- coding: utf-8 -*-
from flectra import api, fields, models


class JobDetails(models.Model):
    _name = "job.details"

    name = fields.Char(string="Job Type")
    job_position = fields.Selection([('trainee', 'trainee'),('developer', 'Developer')], string="Job Position",)
    description = fields.Text(string="Description")

    company_line = fields.Many2one("company.details", string="Company")