class Status:

    def define(self, **kwargs):
        """Specifies "Data definition settings" as the subsequent status topic.

        APDL Command: DEFINE

        Notes
        -----
        This is a status [STAT] topic command.  Status topic commands are
        generated by the GUI and will appear in the log file (Jobname.LOG) if
        status is requested for some items under Utility Menu> List> Status.
        This command will be immediately followed by a STAT command, which will
        report the status for the specified topic.

        If entered directly into the program, the STAT command should
        immediately follow this command.
        """
        command = f"DEFINE,"
        return self.run(command, **kwargs)

    def operate(self, **kwargs):
        """Specifies "Operation data" as the subsequent status topic.

        APDL Command: OPERATE

        Notes
        -----
        This is a status [STAT] topic command.  Status topic commands are
        generated by the GUI and will appear in the log file (Jobname.LOG) if
        status is requested for some items under Utility Menu> List> Status.
        This command will be immediately followed by a STAT command, which will
        report the status for the specified topic.

        If entered directly into the program, the STAT command should
        immediately follow this command.
        """
        command = f"OPERATE,"
        return self.run(command, **kwargs)

    def plotting(self, **kwargs):
        """Specifies "Plotting settings" as the subsequent status topic.

        APDL Command: PLOTTING

        Notes
        -----
        This is a status [STAT] topic command.  Status topic commands are
        generated by the GUI and will appear in the log file (Jobname.LOG) if
        status is requested for some items under Utility Menu> List> Status.
        This command will be immediately followed by a STAT command, which will
        report the status for the specified topic.

        If entered directly into the program, the STAT command should
        immediately follow this command.
        """
        command = f"PLOTTING,"
        return self.run(command, **kwargs)

    def print(self, **kwargs):
        """Specifies "Print settings" as the subsequent status topic.

        APDL Command: PRINT

        Notes
        -----
        This is a status [STAT] topic command.  Status topic commands are
        generated by the GUI and will appear in the log file (Jobname.LOG) if
        status is requested for some items under Utility Menu> List> Status.
        This command will be immediately followed by a STAT command, which will
        report the status for the specified topic.

        If entered directly into the program, the STAT command should
        immediately follow this command.
        """
        command = f"PRINT,"
        return self.run(command, **kwargs)
