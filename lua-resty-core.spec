%define lua_dir	%{_datarootdir}/lua
%define lua_dir_resty	%{lua_dir}/5.1/resty
%define lua_dir_ngx	%{lua_dir}/5.1/ngx

Name: lua-resty-core
Summary: New FFI-based API for lua-nginx-module
Version: 0.1.23
Release: 1
URL: https://github.com/yoannguion/lua-resty-core
License: BSD
BuildArch: noarch
Requires: lua-resty-lrucache

%description
New FFI-based API for lua-nginx-module

%install
mkdir -p $RPM_BUILD_ROOT%{lua_dir_resty}/core
mkdir -p $RPM_BUILD_ROOT%{lua_dir_ngx}/ssl
cp -rf %{_sourcedir}/lib/resty/* $RPM_BUILD_ROOT%{lua_dir_resty}
cp -rf %{_sourcedir}/lib/ngx/* $RPM_BUILD_ROOT%{lua_dir_ngx}

%files
%{lua_dir_ngx}/ssl/clienthello.lua
%{lua_dir_ngx}/ssl/clienthello.md
%{lua_dir_ngx}/ssl/session.lua
%{lua_dir_ngx}/ssl/session.md
%{lua_dir_ngx}/balancer.lua
%{lua_dir_ngx}/balancer.md
%{lua_dir_ngx}/base64.lua
%{lua_dir_ngx}/base64.md
%{lua_dir_ngx}/errlog.lua
%{lua_dir_ngx}/errlog.md
%{lua_dir_ngx}/ocsp.lua
%{lua_dir_ngx}/ocsp.md
%{lua_dir_ngx}/pipe.lua
%{lua_dir_ngx}/pipe.md
%{lua_dir_ngx}/process.lua
%{lua_dir_ngx}/process.md
%{lua_dir_ngx}/re.lua
%{lua_dir_ngx}/re.md
%{lua_dir_ngx}/req.lua
%{lua_dir_ngx}/req.md
%{lua_dir_ngx}/resp.lua
%{lua_dir_ngx}/resp.md
%{lua_dir_ngx}/semaphore.lua
%{lua_dir_ngx}/semaphore.md
%{lua_dir_ngx}/ssl.lua
%{lua_dir_ngx}/ssl.md
%{lua_dir_resty}/core/base.lua
%{lua_dir_resty}/core/base64.lua
%{lua_dir_resty}/core/ctx.lua
%{lua_dir_resty}/core/exit.lua
%{lua_dir_resty}/core/hash.lua
%{lua_dir_resty}/core/misc.lua
%{lua_dir_resty}/core/ndk.lua
%{lua_dir_resty}/core/phase.lua
%{lua_dir_resty}/core/regex.lua
%{lua_dir_resty}/core/request.lua
%{lua_dir_resty}/core/response.lua
%{lua_dir_resty}/core/shdict.lua
%{lua_dir_resty}/core/socket.lua
%{lua_dir_resty}/core/time.lua
%{lua_dir_resty}/core/uri.lua
%{lua_dir_resty}/core/utils.lua
%{lua_dir_resty}/core/var.lua
%{lua_dir_resty}/core/worker.lua
%{lua_dir_resty}/core.lua





%changelog
* Wed Aug 03 2022 Yoann GUION <yoann.guion@gmail.com> - 0.1.23-1
- Initial release 0.1.23
