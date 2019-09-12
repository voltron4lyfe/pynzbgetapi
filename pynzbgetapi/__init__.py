"""Basic Python wrapper for the NZBGet API"""

__author__ = """Holiest of Hand Grenades"""

import json
import logging
import ssl
from urllib.parse import quote
import xmlrpc.client

_LOGGER = logging.getLogger(__name__)


class NZBGetAPIException(Exception):
    """Top level module exception."""
    pass


class NZBGetAPI:
    """Simple wrapper for NZBGet's API."""

    def __init__(
        self,
        host,
        username=None,
        password=None,
        secure=False,
        verify_certificate=True,
        port=6789,
    ):
        """Initialize NZBGet API and set headers needed later."""

        ssl = "s" if secure else ""

        if username is not None and password is not None:
            url = (
                f"http{ssl}://{quote(username)}:{quote(password)}@{host}:{port}/xmlrpc"
            )
        else:
            url = f"http{ssl}://{host}:{port}/xmlrpc"

        if secure and not verify_certificate:
            ssl_ctx = ssl.create_default_context()
            ssl_ctx.check_hostname = False
            ssl_ctx.verify_mode = ssl.CERT_NONE

            self.proxy = xmlrpc.client.ServerProxy(url, context=ssl_ctx)
        else:
            self.proxy = xmlrpc.client.ServerProxy(url)

    def __proxy_call(self, method_call):
        try:
            # Internal method to transalte xmlrpc exceptions to library ones.
            return method_call()
        except (xmlrpc.client.Error, ConnectionError) as err:
            raise NZBGetAPIException(str(err)) from None

    def version(self):
        """Get Version"""
        return self.__proxy_call(lambda: self.proxy.version())

    def shutdown(self):
        """Shutdown NZBGet"""
        return self.__proxy_call(lambda: self.proxy.shutdown())

    def reload(self):
        """Reload NZBGet"""
        return self.__proxy_call(lambda: self.proxy.reload())

    def listgroups(self, number_of_log_entries):
        """Get current groups (NZB Files)"""
        return self.__proxy_call(lambda: self.proxy.listgroups(number_of_log_entries))

    def listfiles(self, nzbid):
        """Get file list from an nzbfile"""
        return self.__proxy_call(lambda: self.proxy.listfiles(0, 0, nzbid))

    def history(self, hidden=False):
        """Get History"""
        return self.__proxy_call(lambda: self.proxy.history(hidden))

    def append(
        self,
        nzbfilename,
        nzbcontent,
        category,
        priority,
        add_to_top,
        add_paused,
        dupe_key,
        dupe_score,
        dupe_mode,
        pp_parameters,
    ):
        """Append an NZB to the queue."""
        return self.__proxy_call(
            lambda: self.proxy.append(
                nzbfilename,
                nzbcontent,
                category,
                priority,
                add_to_top,
                add_paused,
                dupe_key,
                dupe_score,
                dupe_mode,
                pp_parameters,
            )
        )

    def editqueue(self, command, param, ids):
        """Edit the queue."""
        return self.__proxy_call(lambda: self.proxy.editqueue(command, param, ids))

    def scan(self):
        """Scan the nzbdirectory."""
        return self.__proxy_call(lambda: self.proxy.scan())

    def status(self):
        """Get Status."""
        return self.__proxy_call(lambda: self.proxy.status())

    def log(self, id_from, number_of_entries):
        """Return the log."""
        return self.__proxy_call(lambda: self.proxy.log(id_from, number_of_entries))

    def writelog(self, kind, text):
        """Write a new log message."""
        return self.__proxy_call(lambda: self.proxy.writelog(kind, text))

    def loadlog(self, nzbid, id_from, number_of_entries):
        """Return nzbg-log for a specific nzb-file."""
        return self.__proxy_call(
            lambda: self.proxy.loadlog(nzbid, id_from, number_of_entries)
        )

    def servervolumes(self):
        """Collect newsserver historical transfer statistics."""
        return self.__proxy_call(lambda: self.proxy.servervolumes())

    def resetservervolume(self, server_id, sounter):
        """Reset newsserver historical transfer statistics."""
        return self.__proxy_call(
            lambda: self.proxy.resetservervolume(server_id, sounter)
        )

    def rate(self, limit):
        """Set transfer limit."""
        return self.__proxy_call(lambda: self.proxy.rate(limit))

    def pausedownload(self):
        """Pause download queue."""
        return self.__proxy_call(lambda: self.proxy.pausedownload())

    def resumedownload(self):
        """Resume downloads."""
        return self.__proxy_call(lambda: self.proxy.resumedownload())

    def pausepost(self):
        """Pause post-processing."""
        return self.__proxy_call(lambda: self.proxy.pausepost())

    def resumescan(self):
        """Resume previously paused scanning for new nzbfiles."""
        return self.__proxy_call(lambda: self.proxy.resumescan())

    def scheduleresume(self, seconds):
        """Schedule resume after expiring of wait interval."""
        return self.__proxy_call(lambda: self.proxy.scheduleresume(seconds))

    def config(self):
        """Get current config."""
        return self.__proxy_call(lambda: self.proxy.config())

    def loadconfig(self):
        """Read configuration file from disk."""
        return self.__proxy_call(lambda: self.proxy.loadconfig())

    def saveconfig(self, options):
        """Save configuration file to disk."""
        return self.__proxy_call(lambda: self.proxy.saveconfig(options))

    def configtemplates(self, load_from_disk):
        """Return configuration file template and configuration sections"""
        return self.__proxy_call(lambda: self.proxy.configtemplaes(load_from_disk))
