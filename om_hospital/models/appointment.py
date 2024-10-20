from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread']
    _description = "Hospital Appointment"
    _rec_name = 'patient_id'

    reference = fields.Char(string="Reference", default="New")
    patient_id = fields.Many2one('hospital.patient', string="Patient")
    date_appintment = fields.Date(string="Date")
    note = fields.Text(string="Note")
    state = fields.Selection([
        ('draft','Draft'),('confirmed','Confirmed'),('ongoing','On Going'),('done','Done'),('cancelled','Cancelled')
        ], default='draft', tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        print("mohtashim", vals_list)
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == "New":
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super().create(vals_list)

    def action_confirm(self):
        for rec in self:
           rec.state = "confirmed"
    
    def action_ongoing(self):
        for rec in self:
            self.state = 'ongoing'
    
    def action_done(self):
        for rec in self:
            self.state = "done"

    def action_cancelled(self):
        for rec in self:
            self.state = 'cancelled'

