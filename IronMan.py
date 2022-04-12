using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Web04
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        SqlConnection Conn = new SqlConnection("Data Source=.;Initial Catalog=Web01;Integrated Security=True");
        protected void Page_Load(object sender, EventArgs e)
        {
            DataTable dt = new DataTable();
            SqlCommand cmd = new SqlCommand("SELECT * FROM web3", Conn);
            SqlDataAdapter da = new SqlDataAdapter(cmd);
            da.Fill(dt);
            grdRecord.DataSource = dt;
            grdRecord.DataBind();
        }
        private void GetRecord(int id)
        {
            DataTable dt = new DataTable();
            SqlCommand cmd = new SqlCommand("SELECT * FROM web3 where id='" + id + "'", Conn);
            SqlDataAdapter da = new SqlDataAdapter(cmd);
            da.Fill(dt);
            if (dt.Rows.Count > 0)
            {
                txt_name.Text = dt.Rows[0]["name"].ToString();
                txt_address.Text = dt.Rows[0]["address"].ToString();
                txt_email.Text = dt.Rows[0]["email"].ToString();
                txt_contact.Text = dt.Rows[0]["contact"].ToString();

            }
        }

        protected void btn_fetch_Click(object sender, EventArgs e)
        {
            int id = Convert.ToInt32(txt_id.Text);
            GetRecord(id);
        }

        protected void btn_insert_Click(object sender, EventArgs e)
        {
            SqlCommand cmd = new SqlCommand("INSERT INTO web3 (name,email,address,contact)VALUES(@name,@email,@address,@contact)",Conn);
            cmd.Parameters.AddWithValue("@name", txt_name.Text);
            cmd.Parameters.AddWithValue("@email", txt_email.Text);
            cmd.Parameters.AddWithValue("@address", txt_address.Text);
            cmd.Parameters.AddWithValue("@contact", txt_contact.Text);
            Conn.Open();
            cmd.ExecuteNonQuery();
            Conn.Close();
            Page_Load(sender, e);
        }

        protected void btn_update_Click(object sender, EventArgs e)
        {
            SqlCommand cmd = new SqlCommand("UPDATE web3 SET name=@name, email=@email, address=@address, contact=@contact WHERE id='"+txt_id.Text+"'", Conn);
            cmd.Parameters.AddWithValue("@id", txt_id.Text);
            cmd.Parameters.AddWithValue("@name", txt_name.Text);
            cmd.Parameters.AddWithValue("@email", txt_email.Text);
            cmd.Parameters.AddWithValue("@address", txt_address.Text);
            cmd.Parameters.AddWithValue("@contact", txt_contact.Text);
            Conn.Open();
            cmd.ExecuteNonQuery();
            Conn.Close();
            Page_Load(sender, e);
        }

        protected void btn_delete_Click(object sender, EventArgs e)
        {
            SqlCommand cmd = new SqlCommand("DELETE FROM web3 WHERE id=@id", Conn);
            cmd.Parameters.AddWithValue("@id", txt_id.Text);
            Conn.Open();
            cmd.ExecuteNonQuery();
            Conn.Close();
            Page_Load(sender, e);
        }
    }
}
