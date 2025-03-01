import streamlit as st

# about_page = st.Page(
#     "about/about_user.py",
#     title="About Me",
#     icon=":material/settings:",
#     )
# about_people_page = st.Page(
#     "about/about_people.py",
#     title="About people",
#     icon=":material/settings:",
#     )





pages = { "Overview":[
          st.Page("docs/overview/overview.py", title="Overview", icon="🔥",)
    ],
         
    "Getting Started": [
        st.Page("docs/get_started/installation/installation.py", title="Installation", icon="🔥",),
        st.Page("docs/get_started/projects_setup/projects_setup.py", title="Projects Setup", icon="🔥",),
        st.Page("docs/get_started/users_setup/users_setup.py", title="Users Setup", icon="🔥",),
        st.Page("docs/get_started/systems_setup/systems_setup.py", title="Systems Setup", icon="🔥",),
        st.Page("docs/get_started/environment_setup/environment_setup.py", title="Environment" , icon="🔥",),
    ],
    "User Guide": [
        st.Page("docs/user_guide/user_login/user_login.py", title="User Login & Logout", icon="🔥",),
        st.Page("docs/user_guide/time_logs/time_logs.py", title="User Time Logs", icon="🔥",),
        st.Page("docs/user_guide/it_ticketing/it_ticketing.py", title="IT Ticketing", icon="🔥",),
        st.Page("docs/user_guide/tech_ticketing/tech_ticketing.py", title="Tech Ticketing", icon="🔥",),
    ],
    "Project Management": [
        st.Page("docs/proj_manag/project_schedule/project_schedule.py", title="Project Schedule", icon="🔥",), 
        st.Page("docs/proj_manag/reviewer_setup/reviewer_setup.py", title="Reviewer Setup", icon="🔥",), 
        st.Page("docs/proj_manag/asset_ingestion/asset_ingestion.py", title="Add Asset Ingestion", icon="🔥",),
        st.Page("docs/proj_manag/seq_shots_ingestion/seq_shots_ingestion.py", title="Seq/Shots Ingestion", icon="🔥",),  
        st.Page("docs/proj_manag/push_to_tasks/push_to_tasks.py", title="Push to Tasks View", icon="🔥",),      
        st.Page("docs/proj_manag/task_assignments/task_assignments.py", title="Task Assignments", icon="🔥",), 
    ],
    "Creative Developments": [
        st.Page("docs/cret_dev/artist_task_view/artist_task_view.py", title="Artist Task View", icon="🔥",),
        st.Page("docs/cret_dev/art_developments/art_developments.py", title="Art & Developments", icon="🔥",),
        st.Page("docs/cret_dev/open_dcc/open_dcc.py", title="Open DCC Apps", icon="🔥",),
        st.Page("docs/cret_dev/self_reviewing/self_reviewing.py", title="Self Reviewing", icon="🔥",),
        st.Page("docs/cret_dev/sending_reviewer/sending_reviewer.py", title="Sending Reviewer", icon="🔥",),
        st.Page("docs/cret_dev/reworks/reworks.py", title="Reworks", icon="🔥",),
    ],
    "Status Display": [
        st.Page("docs/status_dis/artist_task_display.py", title="Artist Task Display", icon="🔥",),
        st.Page("docs/status_dis/overall_status.py", title="Overall Status", icon="🔥",),
    ],
    "Production Tracking": [
        st.Page("docs/prod_tracking/task_progress.py", title="Task Progress Page", icon="🔥",),
        st.Page("docs/prod_tracking/status_change.py", title="Status Change Page", icon="🔥",),
    ],
    # "DCC Publishing": [
    #     st.Page("docs/maya.py", title="Maya"),
    #     st.Page("docs/unreal.py", title="Unreal"),
    #     st.Page("docs/substance.py", title="Substance"),
    #     st.Page("docs/nuke.py", title="Nuke"),
    #     st.Page("docs/houdini.py", title="Houdini"),
    #     st.Page("docs/blender.py", title="Blender"),
    # ],
}
#doc_pages = [Overview]
#pg = st.navigation({"HOME": pages})
#pg = st.navigation(pages.keys : pages.items())
pg = st.navigation(pages)
pg.run()
